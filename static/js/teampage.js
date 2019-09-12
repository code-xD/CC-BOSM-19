
var refbut=document.getElementById("refbut");
var teamname=document.getElementById("teamname");


function teamname {
    var xhr=new XMLHttpRequest();
    xhttp.open("GET", "linkhere", true);
    xhr.setRequestHeader("Content-Type",'application/json');
    xhr.onreadystatechange=function() {
        if (this.readyState==4 && this.status==200)
        var json1 = JSON.parse(this.responseText);
        document.getElementById("teamname").innerHTML = json.team_name;
    }
    xhr.send();
}

var players= new Array(15);
var i=0;

refbut.addEventListener("click", addteam);


function addteam(){
    var xhttp = new XMLHttpRequest();


    xhttp.open("GET", "linkhere", true);


    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           var json2 = JSON.parse(this.responseText);
           
           var players[i]=document.createElement("p");
           players[i].classList.add("players");
           players[i].innerHTML="Name: "+this.responseText;
           last.appendChild(btn);
        }
    };
    xhttp.send();
    i++;
}
