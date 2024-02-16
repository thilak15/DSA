# Write your MySQL query statement below
SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b ON a.id = b.id - 1 -- Join with the next row
JOIN Logs c ON a.id = c.id - 2 -- Join with the row after the next
WHERE a.num = b.num AND a.num = c.num;
