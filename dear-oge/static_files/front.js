function question() {
  $("output").click(oge_response)
}

window.onload = function() {
    document.getElementById("my_audio").play();
}

function neutral_call() {
  $.get("https://steakovercooked.com/api/fortune/", function (data) {
  $("#output").text(data);
  }
)
}
