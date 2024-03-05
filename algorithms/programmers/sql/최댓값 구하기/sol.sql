SELECT DATETIME
FROM ANIMAL_INS
WHERE DATETIME = ( select max(datetime) FROM animal_ins)