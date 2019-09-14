function joinTeam(){
  var xhttp = new XMLHttpRequest();
  var obj = {
    pin:document.getElementsByClassName("input2")[0].value
  }
  var pincode=JSON.stringify(obj)
  xhttp.open("POST", "jointeam/", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };

  xhttp.send(pincode);
}
