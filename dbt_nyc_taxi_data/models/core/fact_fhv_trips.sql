{{ config(materialized="table") }}


with pickup_zone as (
        select locationid, borough as pickup_borough, zone as pickup_zone
        from {{ ref("dim_zones") }}
        where borough != 'Unknown'
),
dropoff_zone as (
    select locationid, borough as dropoff_borough, zone as dropoff_zone
    from {{ ref("dim_zones") }}
    where borough != 'Unknown'
)
select
    dispatching_base_num,
    pickup_zone.pickup_borough,
    pickup_zone.pickup_zone,
    dropoff_zone.dropoff_borough,
    dropoff_zone.dropoff_zone,
    pickup_datetime,
    dropoff_datetime,
from {{ ref("stg_fhv_tripdata") }}
inner join pickup_zone on stg_fhv_tripdata.pickup_locationid= pickup_zone.locationid
inner join dropoff_zone on stg_fhv_tripdata.dropoff_locationid = dropoff_zone.locationid