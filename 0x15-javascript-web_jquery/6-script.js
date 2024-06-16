// Updating header content when clicking an 'DIV#update_header' element

function updateHeader () {
  $('header').text('New Header!!!');
}

$('DIV#update_header').on('click', updateHeader);
