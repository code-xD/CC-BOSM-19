function team() {
    var xhttp1 = new XMLHttpRequest();
var team_name = JSON.stringify(document.getElementsByClassName("input2").innerHTML);
xhttp1.open("POST", "url", true);
xhttp1.setRequestHeader("Content-Type", "application/json");
xhttp1.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  }
};

xhttp1.send(team_name);
}

var xhttp2 = new XMLHttpRequest();
xhhtp2.open("GET","url",true);
xhttp2.setRequestHeader("Content-Type", "application/json");
xhttp2.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
      var json = JSON.parse(this.responseText);
      console.log(json);
      var pin = json.pin;
      document.getElementById("").innerHTML = pin;
  }
};
xhttp2.send();