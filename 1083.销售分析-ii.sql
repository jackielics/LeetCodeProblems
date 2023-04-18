--
-- @lc app=leetcode.cn id=1083 lang=mysql
--
-- [1083] 销售分析 II
--

-- @lc code=start
# Write your MySQL query statement below
WITH Sales_Prod AS
(SELECT 	*
FROM 	Sales
		LEFT JOIN Product
		USING(product_id))

SELECT 	DISTINCT buyer_id
FROM 	Sales_Prod
WHERE 	buyer_id IN(SELECT buyer_id
						FROM Sales_Prod
						WHERE product_name = 'S8')
		AND buyer_id NOT IN(SELECT buyer_id
							FROM Sales_Prod
							WHERE product_name = 'iPhone')
-- @lc code=end

