-- Determing average temperature for each city

USE hbtn_0c_0;

SELECT city, AVG(value) AS avg_temp
FROM temeratures GROUP BY city
ORDER BY avg_temp DESC;
