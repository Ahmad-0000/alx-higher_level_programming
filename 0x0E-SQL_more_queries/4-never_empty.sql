-- This is a script to create a table with the name "id_not_null"
-- in which the 'id' field is default to 1, if the table exists
-- it will not fail

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(265));
