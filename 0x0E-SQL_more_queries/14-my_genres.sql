-- This is a script to show all the the names of the genres that
-- the TV show "Dexter" has in the database "hbtn_0d_tvshows".
SELECT name
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
