# Answer of Question 1 

CREATE MATERIALIZED VIEW vw_agg_trip_zone AS
    SELECT 
        AVG(tpep_dropoff_datetime - tpep_pickup_datetime) AS avg_trip_time,
        MIN(tpep_dropoff_datetime - tpep_pickup_datetime) AS min_trip_time,
        MAX(tpep_dropoff_datetime - tpep_pickup_datetime) AS max_trip_time,
        pulocationid,
        dolocationid
    FROM trip_data
    WHERE tpep_dropoff_datetime > tpep_pickup_datetime
    GROUP BY pulocationid, dolocationid;

WITH t AS (
    SELECT
        MAX(avg_trip_time) AS max_avg,
        pulocationid,
        dolocationid 
    FROM vw_agg_trip_zone
    GROUP BY pulocationid, dolocationid
    ORDER BY max_avg DESC
    LIMIT 1
)
SELECT pu_taxi_zone.zone AS pickup_zone, do_taxi_zone.zone AS dropoff_zone
FROM t
JOIN taxi_zone AS pu_taxi_zone
    ON t.pulocationid = pu_taxi_zone.location_id
JOIN taxi_zone AS do_taxi_zone
    ON t.dolocationid = do_taxi_zone.location_id;

--   pickup_zone   | dropoff_zone
-- ----------------+--------------
--  Yorkville East | Steinway        

# Answer of Question 2

CREATE MATERIALIZED VIEW vw_Number_of_trips AS
    SELECT 
        COUNT(*) AS num_trips,
        AVG(tpep_dropoff_datetime - tpep_pickup_datetime) AS avg_trip_time,
        MIN(tpep_dropoff_datetime - tpep_pickup_datetime) AS min_trip_time,
        MAX(tpep_dropoff_datetime - tpep_pickup_datetime) AS max_trip_time,
        pulocationid,
        dolocationid
    FROM trip_data
    WHERE tpep_dropoff_datetime > tpep_pickup_datetime
    GROUP BY pulocationid, dolocationid;

WITH t AS (
    SELECT MAX(avg_trip_time) AS max_avg, pulocationid, dolocationid 
    FROM vw_Number_of_trips
    GROUP BY pulocationid, dolocationid
    ORDER BY max_avg DESC
    LIMIT 1
)
SELECT atz.num_trips
FROM t
JOIN agg_trip_zone AS atz
    ON t.pulocationid = atz.pulocationid AND t.dolocationid = atz.dolocationid;

--  num_trips
-- -----------
--          1

# Answer of Question 3
CREATE MATERIALIZED VIEW vw_Top_3_busiest_zones AS
    SELECT MAX(tpep_pickup_datetime) AS pickup_datetime
    FROM trip_data;

-- CREATE_MATERIALIZED_VIEW

WITH t AS (
    SELECT
        COUNT(*) AS num_trips,
        trip_data.pulocationid
    FROM vw_Top_3_busiest_zones, trip_data
    WHERE trip_data.tpep_pickup_datetime > ( vw_Top_3_busiest_zones.pickup_datetime - interval '17 hours')
    GROUP BY trip_data.pulocationid
    ORDER BY 1 DESC
    LIMIT 3
)
SELECT taxi_zone.zone
FROM t
JOIN taxi_zone AS taxi_zone
    ON t.pulocationid = taxi_zone.location_id;

--         zone
-- ---------------------
--  LaGuardia Airport
--  Lincoln Square East
--  JFK Airport
