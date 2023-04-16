--
-- @lc app=leetcode.cn id=1327 lang=mysql
--
-- [1327] 列出指定时间段内所有的下单产品
--

-- @lc code=start
# Write your MySQL query statement below
EXPLAIN SELECT 	product_name, 
		SUM(unit) AS unit
FROM 	Orders O
		LEFT JOIN	Products P
		USING(product_id)
WHERE 	order_date LIKE "2020-02%"
GROUP BY	product_id
HAVING 		SUM(unit) >= 100
-- @lc code=end

