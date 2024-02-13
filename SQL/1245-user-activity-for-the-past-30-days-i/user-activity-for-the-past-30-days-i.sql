# Write your MySQL query statement below
select activity_date as day,
Count(Distinct user_id) as active_users
From Activity
Where datediff('2019-07-27',activity_date)<30
And activity_date<='2019-07-27'
Group by activity_date