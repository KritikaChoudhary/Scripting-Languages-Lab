function check(){
  var v1=document.getElementById('usn').value;
  var v2=document.getElementById('dob').value;
  var v3=document.getElementById('m1').value
  var v4=document.getElementById('m2').value;
  var v5=document.getElementById('m3').value;
  if(v1=="" || v2=="" || v3=="" || v4=="" || v5=="")
    document.getElementById('msg').innerHTML="Enter all the details"
  }
