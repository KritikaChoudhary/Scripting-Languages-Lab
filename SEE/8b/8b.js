var hosp=
  {
    "hospital_location":"Saraswati",
    "location":"Indira Road"
  };

var patient={
  "Name":"Nancy",
  "AadharNumber":123456,
  "labtests":["Blood","Urine"]
};
window.onload=function(){
  document.getElementById("name").innerHTML=hosp.hospital_location;
  document.getElementById("loc").innerHTML=hosp.location;
}
function change(x){
  x.style.color="red";
  document.getElementById("p").removeAttribute("hidden");
  document.getElementById("n").innerHTML=patient.Name;
  document.getElementById("an").innerHTML=patient.AadharNumber;
  var lt="";
  for ( i in patient.labtests)
    lt+=patient.labtests[i]+" ";
  document.getElementById("lt").innerHTML=lt;
}
function back(x){
  x.removeAttribute("style");
  document.getElementById("p").hidden=true;
}
