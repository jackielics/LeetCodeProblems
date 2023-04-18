--
-- @lc app=leetcode.cn id=1070 lang=mysql
--
-- [1070] 产品销售分析 III
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	product_id, 
		first_year, 
		quantity, 
		price
FROM	
(SELECT	product_id, 
		`year`, 
		MIN(`year`) OVER(PARTITION BY product_id ) AS first_year, 
		quantity, 
		price
FROM 	Sales ) AS T
WHERE	`year` = first_year

-- @lc code=end

