CREATE OR REPLACE EXTERNAL TABLE `ny_taxi.green_taxi_data`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://my_taxi_rides_nyc/nyc_taxi_data/*.parquet']
);


SELECT count(*) FROM `ny_taxi.green_taxi_data` ;

CREATE OR REPLACE TABLE `ny_taxi.native_green_taxi_data` AS
SELECT
  *,
FROM `ny_taxi.green_taxi_data`;

CREATE OR REPLACE VIEW `ny_taxi.temp_view` AS
SELECT
  *,
  DATE(TIMESTAMP(lpep_pickup_datetime)) AS pickup_date
FROM
  `ny_taxi.green_taxi_data`;

-- Create the partitioned table based on the temporary view
CREATE OR REPLACE TABLE `ny_taxi.native_green_taxi_data_partitioned`
PARTITION BY pickup_date
CLUSTER BY PUlocationID AS
  (
    SELECT *
    FROM `ny_taxi.temp_view`
  );

SELECT count(*) FROM ny_taxi.native_green_taxi_data WHERE fare_amount = 0;
SELECT COUNT(DISTINCT PULocationID) FROM `ny_taxi.native_green_taxi_data`;
SELECT COUNT(DISTINCT PULocationID) FROM `ny_taxi.green_taxi_data`;

SELECT
  DISTINCT PULocationID
FROM
  `ny_taxi.native_green_taxi_data`
WHERE
  DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';


SELECT
  DISTINCT PULocationID
FROM
  `ny_taxi.native_green_taxi_data_partitioned`
WHERE
  DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

