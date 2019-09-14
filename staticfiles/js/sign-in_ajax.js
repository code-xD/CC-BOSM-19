function sendtoken() {
  var obj = {
  id : token
}
var send = JSON.stringify(obj);
var res = new XMLHttpRequest();
res.open("POST","/treasure/login/",true);
res.setRequestHeader("Content-Type","application/json");
res.onreadystatechange = function() {
  if (this.readyState ==4 && this.status == 200) {
    var check = JSON.parse(this.responseText);
    console.log(check);
  }
};
res.send(send);
};
