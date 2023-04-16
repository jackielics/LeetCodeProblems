--
-- @lc app=leetcode.cn id=1821 lang=mysql
--
-- [1821] 寻找今年具有正收入的客户
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	DISTINCT customer_id
FROM	Customers
WHERE 	year = 2021
		AND revenue > 0
-- @lc code=end

