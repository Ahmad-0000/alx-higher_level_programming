-- This is a script to create the table "unique_id" in which the field
-- "id" is unique and has a default value of 1

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(265));
