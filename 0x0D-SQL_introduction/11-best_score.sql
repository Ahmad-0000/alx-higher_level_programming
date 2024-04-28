-- This is a script to list the attributes "score" and "name" of the
-- records having a score >= 10 from the table "second_table" in the
-- current database in descending order regarding "score"

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
