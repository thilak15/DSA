# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN MOD(id, 2) = 0 THEN id - 1
        -- For odd ids, check if it's the last id. If not, swap with the next id.
        WHEN id = (SELECT MAX(id) FROM Seat) AND MOD(id, 2) = 1 THEN id
        ELSE id + 1
    END AS id,
    student
FROM Seat
ORDER BY id ASC;
