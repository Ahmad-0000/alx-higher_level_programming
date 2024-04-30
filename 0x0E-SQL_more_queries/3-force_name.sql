-- This is a script to create a table named "force_name" if it
-- doesn't exit

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL);
