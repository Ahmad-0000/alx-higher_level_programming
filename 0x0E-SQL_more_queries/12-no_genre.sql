-- This is a script to list all the tv show titles that has no genre
-- linked to them in the database "hbtn_0d_tvshows" using "LEFT JOIN"
-- technique
SELECT ts.title, tsg.genre_id
FROM tv_shows ts LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
WHERE tsg.show_id IS NULL
ORDER BY ts.title ASC, tsg.genre_id ASC;
