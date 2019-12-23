function sub(){
  var o=document.getElementById("onion").value;
  var t=document.getElementById("tom").value;
  var p=document.getElementById("pot").value;
  console.log(o+t+p);
  document.getElementById("msg").innerHTML=60*o+50*t+40*p;
}
