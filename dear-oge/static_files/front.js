

function question() {
  $("output").click(oge_response)
}

window.onload = function() {
    document.getElementById("my_audio").play();
}


$(function(){
  $("#dropDownBtn").on("change",function() {
    $(".links").hide();
    $(".links."+this.value).show();
  });
});


function neutral_call(user, text) {
  $.get("https://steakovercooked.com/api/fortune/", function (data) {
    $("#output").text(data);
  //  $.put("/", {out: data, user:user, text:text})
  $.ajax({
    url: '/neut',
    type: 'POST',
    data: JSON.stringify({
      out: data, user:user, text:text
    }),
    contentType: "application/json; charset=utf-8",
    dataType   : "json",
    success: function(result) {
    }
});
  }
)
}
