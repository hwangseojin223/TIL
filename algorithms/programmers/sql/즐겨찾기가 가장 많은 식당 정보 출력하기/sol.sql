SELECT food_type, rest_id, rest_name, favorites
from rest_info
where (food_type, favorites) in (
    select food_type, max(favorites)
    from rest_info
    group by food_type
)
order by food_type desc

-- sol2
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE FAVORITES IN (
    SELECT MAX(FAVORITES)
    FROM REST_INFO 
    GROUP BY FOOD_TYPE 
    ORDER BY FAVORITES DESC)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC