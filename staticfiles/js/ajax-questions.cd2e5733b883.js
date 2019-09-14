
var xhttp = new XMLHttpRequest();
var question;
var team_name;
xhttp.open("GET", "url/", true);
xhttp.setRequestHeader("Content-Type", "application/json");
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {

    var json = JSON.parse(this.responseText);
    console.log(json);
      question = json.question;
      team_name = json.team_name;
      document.getElementById("q-text").innerHTML = question;
    //  document.getElementsByClassName("").innerHTML = team_name;
      console.log(question,team_name);
  }
};

xhttp.send();

function sendres() {
    var obj = {
      ans : document.getElementsByClassName("input2")[1].value
    }
    console.log(obj);
    var sendans = JSON.stringify(obj);
    var res = new XMLHttpRequest();
    res.open("POST","url/",true);
    res.setRequestHeader("Content-Type", "application/json");
    res.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var flag = JSON.parse(this.responseText).flag;
            console.log(flag)
            if(flag == 1) {
              window.location.href = "http://localhost:8000/treasure/question-main.html";
            } else {
              alert("Incorrect answer was submitted by a crew member!");
            }
        }
    };
    res.send(sendans);
}
