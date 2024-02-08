SELECT P.project_id,
       ROUND(AVG(E.experience_years), 2) AS average_years
FROM Project AS P
INNER JOIN Employee AS E ON P.employee_id = E.employee_id
WHERE E.experience_years IS NOT NULL
GROUP BY P.project_id;
