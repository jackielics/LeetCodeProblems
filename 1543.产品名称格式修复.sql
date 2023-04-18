--
-- @lc app=leetcode.cn id=1543 lang=mysql
--
-- [1543] 产品名称格式修复
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	LOWER(TRIM(product_name)) AS product_name,
		LEFT(sale_date, 7) AS sale_date, 
		COUNT(sale_id) AS total
FROM	Sales
GROUP BY	LEFT(sale_date, 7), LOWER(TRIM(product_name))
ORDER BY 	product_name  ASC, sale_date ASC
-- @lc code=end

