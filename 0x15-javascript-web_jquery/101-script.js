// Manipulation "ul" items

$(function () {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>item</li>');
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').on('click', () => {
    $('UL.my_list').empty();
  });
});
