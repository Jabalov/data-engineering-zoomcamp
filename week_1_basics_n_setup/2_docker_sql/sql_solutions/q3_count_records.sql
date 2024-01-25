SELECT COUNT(*) AS trip_count
FROM green_taxi_data
WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
  AND DATE(lpep_dropoff_datetime) = '2019-09-18';
