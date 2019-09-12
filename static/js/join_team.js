function joinTeam(){
  var xhttp = new XMLHttpRequest();
  var obj = {
    pin:document.getElementsByClassName("input").innerHTML
  }
  xhttp.open("POST", "treasure/jointeam/", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };

  xhttp.send(obj);
}
