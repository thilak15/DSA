# Write your MySQL query statement below
select R.contest_id, round((count(R.user_id)/(SELECT COUNT(DISTINCT user_id) FROM Users)*100),2) as percentage
From Users U join Register R on U.user_id=R.user_id
group by contest_id
order by percentage desc,contest_id 