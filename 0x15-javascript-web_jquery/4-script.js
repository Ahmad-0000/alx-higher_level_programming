// Toggle header element class when clicking DIV#toggle_header element
$('DIV#toggle_header').on('click', toggleClass);

function toggleClass () {
  const header = $('header');
  if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  } else {
    header.removeClass('red');
    header.addClass('green');
  }
}
