SELECT
    a.employee_id AS employee_id,
    a.name AS name,
    COUNT(b.employee_id) AS reports_count,
    ROUND(AVG(b.age)) AS average_age
FROM Employees a
INNER JOIN Employees b ON a.employee_id = b.reports_to
GROUP BY employee_id
order BY employee_id
