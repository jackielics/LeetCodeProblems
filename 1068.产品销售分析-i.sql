--
-- @lc app=leetcode.cn id=1068 lang=mysql
--
-- [1068] 产品销售分析 I
--

-- @lc code=start
# Write your MySQL query statement below

SELECT  product_name, 
        `year`, 
        price
FROM    Sales 
        LEFT JOIN Product 
        USING (product_id)
-- @lc code=end

