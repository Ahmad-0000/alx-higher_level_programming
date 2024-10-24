-- This is a script to create a table named "second_table" in the
-- current database and fill it with some records.

CREATE TABLE IF NOT EXISTS second_table (
id INTEGER,
name VARCHAR(256),
score INTEGER
);

INSERT INTO second_table VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
