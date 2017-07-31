var quotes = [
  'If something is too hard, either you are not doing it right or it is not worth doing',
  'Communication is key in any relationship',
  'Think about how the other person feels',
  'The opportunity for success is there - you just need to acknowledge its presence and grasp it',
  'You are only as good as you think you are',
];


function question() {
  var randomNumber = Math.floor(Math.random() * (quotes.length));
  document.getElementById("output").innerHTML= quotes[randomNumber];
}

function doneFading(){
  alert ("done fading out");
}




function stuffToDoWhenReady() {
  /*$("#hello").fadeOut(100, doneFading);
  $("#emoji").click(function(){
    $("#emoji").fadeOut(100);*/
  }

}

$(document).ready(stuffToDoWhenReady)
