SELECT ROUND(
         IFNULL(
           (
             SELECT COUNT(DISTINCT a.player_id)
             FROM Activity a
             JOIN (
               SELECT player_id, MIN(event_date) AS first_login
               FROM Activity
               GROUP BY player_id
             ) AS first_logins ON a.player_id = first_logins.player_id
             WHERE DATE_ADD(first_logins.first_login, INTERVAL 1 DAY) = a.event_date
           ) / COUNT(DISTINCT player_id)
         , 0)
       , 2) AS fraction
FROM Activity;
