// Changing color of header element when DIV#red_header is clicked

$('DIV#red_header').on('click', changeToRed);

function changeToRed () {
  $('header').addClass('red');
}
