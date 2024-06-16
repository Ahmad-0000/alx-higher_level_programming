// When focusing and pressing <ENTER> or clicking on "#btn_translation",
// fetching translation of 'Hello' based on 'INPUT#language_code' element
// and writing it into the "DIV#hello" element

$(function () {
  const button = $('INPUT#btn_translate');
  const language = $('INPUT#language_code');
  button.on('click', function fetchData () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language.val();
    $.get(url, (result) => {
      $('DIV#hello').text(result.hello);
    });
  });
  language.on('keypress', function fetchData (event) {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + language.val();
    $.get(url, (result) => {
      if (event.which === 13) {
        $('DIV#hello').text(result.hello);
      }
    });
  });
});
