-- This is a script to list the number of records with the same score
-- in the table "second_table" of the current database under the column
-- "number"
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
