function sendtoken() {
    var obj = {
    id : id_token
  }
  var send = JSON.stringify(obj);
  var res = new XMLHttpRequest();
  res.open("POST","url",true);
  res.setRequestHeader("Content-Type", "application/json");
  res.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {      
      }
  };
  res.send(send);
};