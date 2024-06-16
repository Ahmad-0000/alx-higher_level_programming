// Fetching character name
// from 'https://swapi-api.alx-tools.com/api/people/5/?format=json' and
// displaying it in "DIV#character" element

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (data) {
    $('DIV#character').text(data.name);
  });
