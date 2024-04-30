-- This is a script to list all the tv show titles that are
-- linked to at least one genre on a specific database
SELECT ts.title, tsg.genre_id
FROM tv_shows ts INNER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id ASC;
