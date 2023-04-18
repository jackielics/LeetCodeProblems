--
-- @lc app=leetcode.cn id=1565 lang=mysql
--
-- [1565] 按月统计订单数与顾客数
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	LEFT(order_date, 7) AS `month`, 
		COUNT(DISTINCT order_id) AS `order_count`, 
		COUNT(DISTINCT customer_id) AS `customer_count`
FROM	Orders
WHERE	invoice > 20
GROUP BY	LEFT(order_date, 7)
-- @lc code=end

