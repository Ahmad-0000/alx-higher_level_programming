-- This is a script to create a table named "first_table" , if it
-- doesn't exist in the current MySQL database. The database name
-- should name alongised with the command "mysql" should be piped
-- to the script content
CREATE TABLE IF NOT EXISTS first_table (
id INT,
name VARCHAR(256)
);
