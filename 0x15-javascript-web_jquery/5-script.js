// Appending 'li' to a list when clicking 'DIV#add_item' element

function appendUlItem () {
  $('UL.my_list').append('<li>item</li>');
}

$('DIV#add_item').on('click', appendUlItem);
