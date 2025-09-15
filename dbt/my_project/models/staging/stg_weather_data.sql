with source as(
    select * 
    from {{ source('weather', 'raw_weather_data') }}
),
de_up as (
    select *,
        row_number() over(partition by time order by inserted_at desc) as rn
    from source
)

select 
    id,
    city,
    temperature,
    weather_description,
    wind_speed,
    time as weather_time_local,
    (inserted_at + (utc_offset || ' hours')::interval) as inserted_at_local
from de_up
where rn = 1