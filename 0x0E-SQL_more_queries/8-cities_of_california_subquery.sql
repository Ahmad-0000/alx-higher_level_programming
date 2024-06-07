-- A script to select all the cities from the state 'California'
-- without using the keyword "JOIN"

SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states
       	  	  WHERE name = 'California')
ORDER BY id ASC; 
