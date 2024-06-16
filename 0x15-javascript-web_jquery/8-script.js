// Fetching all movie names from
// "https://swapi-api.alx-tools.com/api/films/?format=json"
// and displaying them as items in 'UL#list_movies'

$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    const films = data.results;
    let film = null;
    for (film of films) {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    }
  });
