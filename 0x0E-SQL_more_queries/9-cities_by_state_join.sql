-- This is a script to show all the cities contined in a particular
-- state from the tables "cities" and "states"

SELECT c.id, c.name, s.name
FROM cities c INNER JOIN states s
WHERE c.state_id = s.id
ORDER BY c.id ASC;
