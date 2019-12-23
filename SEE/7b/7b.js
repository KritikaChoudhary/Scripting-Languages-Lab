window.onload=function(){
  var cars=[{
    "Name":"Lambo",
    "Model":"45T",
    "Price":"$1000",
    "Year":"2000"
  },
{
  "Name":"Mercedes",
  "Model":"43C",
  "Price":"$1050",
  "Year":"1999"
},
{
  "Name":"Nano",
  "Model":"C3X",
  "Price":"$800",
  "Year":"2001"
}];
for(i=0;i<cars.length;i++)
{
  var e=document.createElement("th");
  e.id=cars[i].Model;
  e.innerHTML=cars[i].Model;
  document.getElementById("menu").appendChild(e);
}
cars.forEach(mouse);
function mouse(item)
{
  document.getElementById(item.Model).onmouseover=
  function(){
    document.getElementById("details").removeAttribute("hidden");
    document.getElementById("name").innerHTML=item.Name;
    document.getElementById("model").innerHTML=item.Model;
    document.getElementById("price").innerHTML=item.Price;
    document.getElementById("year").innerHTML=item.Year;

  }
}
}
