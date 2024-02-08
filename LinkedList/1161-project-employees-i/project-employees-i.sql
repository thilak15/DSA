SELECT P.project_id,
       ROUND(
           SUM(COALESCE(E.experience_years, 0)) / 
           (COUNT(P.employee_id) - SUM(CASE WHEN E.experience_years IS NULL THEN 1 ELSE 0 END)), 
           2
       ) AS average_years
FROM Project AS P
LEFT JOIN Employee AS E ON P.employee_id = E.employee_id
GROUP BY P.project_id;
