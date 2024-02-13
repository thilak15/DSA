SELECT MAX(num) as num
FROM Mynumbers
WHERE num NOT IN (
  SELECT num
  FROM Mynumbers
  GROUP BY num
  HAVING COUNT(num) > 1
);
