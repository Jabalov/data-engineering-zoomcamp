SELECT z_drop."Zone" AS dropoff_zone,
       MAX(g."tip_amount") AS max_tip_amount
FROM green_taxi_data AS g
JOIN zones AS z_pickup ON z_pickup."LocationID" = g."PULocationID"
JOIN zones AS z_drop ON z_drop."LocationID" = g."DOLocationID"
WHERE DATE(g."lpep_pickup_datetime") >= '2019-09-01'
  AND DATE(g."lpep_pickup_datetime") < '2019-10-01'
  AND z_pickup."Zone" = 'Astoria'
GROUP BY dropoff_zone
ORDER BY max_tip_amount DESC
LIMIT 1;
