--
-- @lc app=leetcode.cn id=1069 lang=mysql
--
-- [1069] 产品销售分析 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  product_id, 
        SUM(quantity) AS `total_quantity`
FROM    Sales 
        LEFT JOIN Product 
        USING (product_id)
GROUP BY product_id
-- @lc code=end

