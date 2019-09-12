
var xhttp = new XMLHttpRequest();
var question;
var team_name;
xhttp.open("GET", "url", true);
xhttp.setRequestHeader("Content-Type", "application/json");
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {

    var json = JSON.parse(this.responseText);
    console.log(json);
      question = json.question;
      team_name = json.team_name;
      document.getElementsByClassName("").innerHTML = question;
      document.getElementsByClassName("").innerHTML = team_name;
      console.log(question,team_name);
  }
};

xhttp.send();

function sendres() {
    var ans = JSON.stringify(document.getElementById("").innerHTML);
    var res = new XMLHttpRequest();
    res.open("POST","url",true);
    res.setRequestHeader("Content-Type", "application/json");
    res.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {      
        }
    };
    res.send(ans);
}
var check = new XMLHttpRequest();
check.open("GET","url","true");
check.setRequestHeader("Content-Type", "application/json");
check.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var flag = JSON.parse(this.responseText).flag;
    }
};
check.send();