window.onload=function(){
  var author=[
    {
      "Name":"John Doe",
      "Country":"America",
      "Title":"Story of my life",
      "Year":1998
    },
     {
       "Name":"Rakesh Kapoor",
       "Country":"India",
       "Title":"Journey to the Center of the Earth",
       "Year":2007
    },
    {
      "Name":"Lily Allen",
      "Country":"Africa",
      "Title":"The Real Deal",
      "Year":2000
    },
    {
      "Name":"Xiao Ping",
      "Country":"China",
      "Title":"Ayurved:The Truth of Life",
      "Year":2013
    }
  ]
  var n=document.getElementsByClassName("name")
  var c=document.getElementsByClassName("country")
  var t=document.getElementsByClassName("title")
  var y=document.getElementsByClassName("year")
  for(i=0;i<n.length;i++)
  {
    n[i].innerHTML=author[i].Name;
    c[i].innerHTML=author[i].Country;
    t[i].innerHTML=author[i].Title;
    y[i].innerHTML=author[i].Year;
  }

}
