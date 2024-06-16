// Fetching translation of 'Hello' based on 'INPUT#language_code' element
// and writing it into the "DIV#hello" element

$(function () {
  const button = $('INPUT#btn_translate');
  button.on('click', function fetchData () {
    const language = $('INPUT#language_code');
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language.val();
    $.get(url, (result) => {
      $('DIV#hello').text(result.hello);
    });
  });
});
