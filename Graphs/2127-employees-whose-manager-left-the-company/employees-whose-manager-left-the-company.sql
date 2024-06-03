SELECT employee_id
FROM Employees
WHERE manager_id  Not IN (SELECT employee_id FROM Employees)
  AND salary < 30000 order by employee_id
