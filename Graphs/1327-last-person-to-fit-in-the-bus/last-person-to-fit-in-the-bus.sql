With CDE1 as 
(
    select person_name,weight,sum(weight) over (order by turn) as cummulative_weight from queue order by turn
)
select person_name from CDE1 where cummulative_weight<=1000 order by cummulative_weight DESC Limit 1