WITH RECURSIVE re AS (
    select 0 as hour
    union all
    select hour + 1 
    from re 
    where hour < 23
)
select re.hour, count(hour(ao.datetime)) AS COUNT
FROM re left join ANIMAL_OUTS as ao ON re.hour = hour(ao.datetime)
group by re.hour;