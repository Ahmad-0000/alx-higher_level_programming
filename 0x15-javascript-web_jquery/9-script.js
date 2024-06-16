// Fetching data from "https://hellosalut.stefanbohacek.dev/?lang=fr"
// and displaying the value of "hello" in the element "DIV#hello"

$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
