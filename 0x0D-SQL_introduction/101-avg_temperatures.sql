-- Determing average temperature for each city

SELECT city, AVG(value) AS avg_temp
FROM temeratures GROUP BY city
ORDER BY avg_temp DESC;
