function question() {
  $("output").click(oge_response)
}

}


function neutral_call(user, text) {
  $.get("https://steakovercooked.com/api/fortune/", function (data) {
    $("#output").text(data);
  //  $.put("/", {out: data, user:user, text:text})
  $.ajax({
    url: '/',
    type: 'PUT',
    data: JSON.stringify({
      out: data, user:user, text:text
    }),
    contentType: "application/json; charset=utf-8",
    dataType   : "json",
    success: function(result) {
        // Do something with the result
    }
});
  }
)
}
