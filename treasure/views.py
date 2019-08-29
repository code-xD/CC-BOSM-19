from google.oauth2 import id_token
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from .models import *
import SportsCrypt.keyconfig as senv

import json

# team edit view


@csrf_exempt
def login(request):

    if request.method == 'POST':

        try:
            authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        except KeyError:
            return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        if authorization != senv.AUTHORIZATION:
            return JsonResponse({"message": "Invalid Request Source", "status": 0})

        try:                # just to decode JSON properly
            data = json.loads(request.body.decode('utf8').replace("'", '"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

        try:
            token = data['token']
        except KeyError as missing_data:
            return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), "status": 0})

        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), senv.CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            email = idinfo['email']

            try:
                participant = Participant.objects.get(email=email)
                if participant.team:
                    return JsonResponse({"message": "User Login Successful!", "status": 2, "participant id": participant.unique_id})
                else:
                    return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant id": participant.unique_id})
            except Participant.DoesNotExist:
                participant = Participant.objects.create(email=email)
                return JsonResponse({"message": "Participant does not belong to any Team!", "status": 1, "participant id": participant.unique_id})

        except ValueError:
            # Invalid token
            return JsonResponse({"message": "Invalid ID Token passed!", "status": 0})


@csrf_exempt
def team_register(request):
    if request.method == 'POST':
        try:
            authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        except KeyError:
            return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        if authorization != senv.AUTHORIZATION:
            return JsonResponse({"message": "Invalid Request Source", "status": 0})

        try:                # just to decode JSON properly
            data = json.loads(request.body.decode('utf8').replace("'", '"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

        try:
            team_name = data['team_name']
            participants = data['participant_list']
            part_id = data['participant_id']
        except KeyError as missing_data:
            return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

        try:
            participant1 = Participant.objects.get(unique_id=part_id)
        except Participant.DoesNotExist:
            return JsonResponse({"message": "Please login first.", "status": 0})

        if participant1.team:
            return JsonResponse({"message": "Your Team is already Registered.", "status": 0})

        try:
            with transaction.atomic():
                team = Team.objects.create(name=team_name, state=0)
                for participant in participants:
                    participant = Participant.objects.get(email=participant["email"])
                    if participant.team is not None:
                        raise Exception
                    participant.team = team
                    participant.save()
            return JsonResponse({"message": "Team registered successfully", "status": 1, "team_name": team.name})
        except Exception:
            return JsonResponse({"message": "Participant team already exists.", "status": 0})

@csrf_exempt
def question_details(request):
        if request.method == 'POST':
            try:
                authorization = str(request.META['HTTP_X_AUTHORIZATION'])
            except KeyError:
                return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

            if authorization != senv.AUTHORIZATION:
                return JsonResponse({"message": "Invalid Request Source", "status": 0})

            try:
                data = json.loads(request.body.decode('utf8'))
            except Exception:
                return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})

            try:
                part_id = data['participant_id']
            except KeyError as missing_data:
                return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

            try:
                with transaction.atomic():
                    participant = Participant.objects.get(unique_id=part_id)
                    req_question=Question.objects.get(pk=participant.team.state+1)
                return JsonResponse({"question_id":req_question.unique_id,"question_text":req_question.question,"status":1})
            except Exception:
                return JsonResponse({"message": "No such question exists.", "status": 0})
        else:
            return JsonResponse({"message": "A <POST> request to get the question", "status": 0})

@csrf_exempt
def check_question_answer(request):
    if request.method =='POST':
        try:
            authorization = str(request.META['HTTP_X_AUTHORIZATION'])
        except KeyError:
            return JsonResponse({"message": "Authorization Header Missing. Couldn't verify request source", "status": 0})

        if authorization != senv.AUTHORIZATION:
            return JsonResponse({"message": "Invalid Request Source", "status": 0})
        try:
            data = json.loads(request.body.decode("utf-8").replace("'",'"'))
        except Exception:
            return JsonResponse({"message": "Please check syntax of JSON data passed.", "status": 0})
        try:
            question_id = data['question_id']
            participant_id = data['participant_id']
            ans_saved = data['ans']  #there is no answer in the database yet.
        except KeyError as missing_data:
            return JsonResponse({'message': 'Field missing: {0}'.format(missing_data), 'status': 0})

        try:
            with transaction.atomic():
                question = Question.objects.get(unique_id=question_id)
                answer = Answer.objects.get(question=question)
                participant = Participant.objects.get(unique_id=participant_id)
                team = participant.team
            if ans_saved == answer.answer:
                team.state += 1
                team.save()
                answer.times_answered += 1
                answer.save()
                return JsonResponse({"message":"Team answered the question correctly.", "status": 1})
            else:
                return JsonResponse({"message":"Answer is incorrect", "status": 0})
        except:
            return JsonResponse({"message":"Check if the question has been answered", "status":0})
