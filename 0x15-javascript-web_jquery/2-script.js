// Changing header color to read when clicking '#red_header' element

$('#red_header').on('click', changeToRed);

function changeToRed () {
  $('header').css('color', '#ff0000');
}
