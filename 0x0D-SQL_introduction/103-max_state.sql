-- Max temperature for each state

USE hbtn_0c_0;

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
