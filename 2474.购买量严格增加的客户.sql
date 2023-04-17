--
-- @lc app=leetcode.cn id=2474 lang=mysql
--
-- [2474] 购买量严格增加的客户
--

-- @lc code=start
# Write your MySQL query statement below
WITH T AS
(SELECT 	customer_id, 
		YEAR(order_date) AS `year`, 
		SUM(price) AS total_price, 
		/* SUM(price) - SUM(SUM(price)) OVER(PARTITION BY customer_id ORDER BY YEAR(order_date) ASC RANGE 1 PRECEDING) AS diff_price, */
		SUM(price) - LAG(SUM(price), 1, 0) OVER(PARTITION BY customer_id ORDER BY YEAR(order_date) ASC RANGE 1 PRECEDING) AS diff_last_price,
		# 中断必不严格增加
		YEAR(order_date) - ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY YEAR(order_date) ASC) AS rk
FROM 	Orders 
GROUP BY	customer_id, 
			YEAR(order_date))


SELECT	DISTINCT customer_id
FROM	T
WHERE	customer_id NOT IN (
	SELECT 	customer_id
	FROM 	T
	GROUP BY	customer_id
	HAVING	COUNT(DISTINCT rk) > 1
	UNION
	SELECT	DISTINCT	customer_id
	FROM 	T
	WHERE 	diff_last_price <= 0
)


-- @lc code=end

