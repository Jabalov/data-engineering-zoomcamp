SELECT z."Borough",
       SUM(g."total_amount") AS total_amount_sum
FROM green_taxi_data AS g
JOIN zones AS z ON z."LocationID" = g."PULocationID"
WHERE DATE(g."lpep_pickup_datetime") = '2019-09-18'
  AND z."Borough" <> 'Unknown'
GROUP BY z."Borough"
HAVING SUM(g."total_amount") > 50000
ORDER BY total_amount_sum DESC
LIMIT 3;
