WITH CTE1 AS (
  SELECT customer_id, COUNT(DISTINCT product_key) AS cnt
  FROM Customer
  GROUP BY customer_id
),
TotalProductCount AS (
  SELECT COUNT(DISTINCT product_key) AS total_cnt
  FROM Product
)
SELECT c.customer_id
FROM CTE1 c, TotalProductCount t
WHERE c.cnt = t.total_cnt;
