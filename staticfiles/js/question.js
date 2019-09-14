function refreshStatus() {
  var res = new XMLHttpRequest();
  res.open("POST","url/",true);
  res.setRequestHeader("Content-Type", "application/json");
  res.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          var flag = JSON.parse(this.responseText).flag;
          if(flag == 1) {
            window.location.href = "localhost:8000/treasure/question-main.html";
          } else {
            alert("Incorrect answer was submitted by a crew member!");
          }
      }
  };
  res.send();
}
