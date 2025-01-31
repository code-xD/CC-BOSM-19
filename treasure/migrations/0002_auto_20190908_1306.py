# Generated by Django 2.2.4 on 2019-09-08 13:06

from django.db import migrations, models
import treasure.models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='code',
            field=models.PositiveIntegerField(default=treasure.models.generatecode, unique=True),
        ),
        migrations.AddField(
            model_name='team',
            name='participant_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
