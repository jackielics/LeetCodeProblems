--
-- @lc app=leetcode.cn id=1082 lang=mysql
--
-- [1082] 销售分析 I 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	seller_id
FROM 
(SELECT 	seller_id, 
		SUM(price) AS total_price, 
		RANK() OVER(ORDER BY SUM(price) DESC) AS rk
FROM 	Sales 
GROUP BY 	seller_id) AS T
WHERE 	rk =1
-- @lc code=end

