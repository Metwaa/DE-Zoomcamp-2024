# Welcome to DE Zoomcamp 2024 - Module 3 - Home Work
Basicly I uploaded green taxi data using Mage orchestrator as follow:

- used load_green_taxi_data_of_2022.py to load the green taxi data of year 2022
- used green_taxi_data_transform.py to covert lpep_pickup_datetime to datetime & create a new column to used in partitoning
- used green_taxi_data_to_gcs_bucket.py to transfer data to gs in this path (mage-zoomcamp-meto/greentaxi_data_of_2022)
- Finally ingest data using BigQuery by the below commands.

# Creating an external table from gs path
CREATE OR REPLACE EXTERNAL TABLE `airy-cortex-297320.ny_taxi.external_green_tripdata_2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-meto/greentaxi_data_of_2022/*.parquet']);

# Create a BQ table from external table
CREATE OR REPLACE TABLE airy-cortex-297320.ny_taxi.green_tripdata_2022_non_partitoned AS
SELECT * FROM airy-cortex-297320.ny_taxi.external_green_tripdata_2022;

# Answer of question 1
SELECT count(*) TotalRecords FROM airy-cortex-297320.ny_taxi.external_green_tripdata_2022;


# Answer of question 2
SELECT DISTINCT(PULocationID)
FROM airy-cortex-297320.ny_taxi.external_green_tripdata_2022;


SELECT DISTINCT(PULocationID)
FROM airy-cortex-297320.ny_taxi.green_tripdata_2022_non_partitoned;


# Answer of question 3
SELECT count(*) TotalRecords 
FROM airy-cortex-297320.ny_taxi.external_green_tripdata_2022
WHERE fare_amount =0;


# Answer of question 4
CREATE OR REPLACE TABLE airy-cortex-297320.ny_taxi.green_tripdata_2022_partitoned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM airy-cortex-297320.ny_taxi.external_green_tripdata_2022;


# Answer of question 5
SELECT DISTINCT(PULocationID)
FROM airy-cortex-297320.ny_taxi.green_tripdata_2022_non_partitoned
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

SELECT DISTINCT(PULocationID)
FROM airy-cortex-297320.ny_taxi.green_tripdata_2022_partitoned_clustered
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';


# Answer of question 8
SELECT count(*) FROM airy-cortex-297320.ny_taxi.green_tripdata_2022_partitoned_clustered;

This query will process 0 B when run due to partitioning & clustering.

# Big Thanks
No words can describe my gratitude, happiness, appreciation for what presenting for us during this awesome intensive zoomcamp 
