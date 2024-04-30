-- This is a script to show all the tv shows in the database
-- "hbtn_0d_tvshows" with their corresponding genres. If a
-- show has not genre, the genre will be displayed as "NULL"
SELECT title, name
FROM tv_shows ts LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
ORDER BY ts.title ASC, tg.name ASC;
