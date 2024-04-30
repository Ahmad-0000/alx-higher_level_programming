-- This is a script to list all the tv show titles with their genre ids
-- in the database named "hbtn_0d_tvshows". If the show has no genre,
-- the genre will be displayed as (NULL)
SELECT ts.title, tsg.genre_id
FROM tv_shows ts LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id ASC;
