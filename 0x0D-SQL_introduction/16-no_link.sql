-- This is a script to list the number of records with the same score
-- in the table "second_table" of the current database. Reconrder with
-- "name" value NULL will not be listed
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
