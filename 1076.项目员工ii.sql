--
-- @lc app=leetcode.cn id=1076 lang=mysql
--
-- [1076] 项目员工II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	project_id
FROM	Project 
GROUP BY 	project_id
HAVING		COUNT(DISTINCT employee_id) 
			= (	SELECT 	MAX(cnt)
				FROM 
				(
					SELECT COUNT(DISTINCT employee_id) AS cnt
					FROM Project 
					GROUP BY project_id
					) AS T
				)


-- @lc code=end

