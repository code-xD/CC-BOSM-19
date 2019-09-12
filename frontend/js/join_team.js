function joinTeam() {
  var xhttp = new XMLHttpRequest();
  var pin = document.getElementsByClassName("input").innerHTML;
  xhttp.open("POST", "/url", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };

  xhttp.send(pin);
}
