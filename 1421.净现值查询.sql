--
-- @lc app=leetcode.cn id=1421 lang=mysql
--
-- [1421] 净现值查询
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	id, 
		`year`, 
		IFNULL(npv, 0) AS npv
FROM	Queries
		LEFT JOIN	NPV 
		USING(id, `year`)

-- @lc code=end

