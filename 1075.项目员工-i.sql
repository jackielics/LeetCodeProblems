--
-- @lc app=leetcode.cn id=1075 lang=mysql
--
-- [1075] 项目员工 I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	project_id, 
		ROUND(
			SUM(experience_years) / COUNT(*),
		 	2) AS average_years
FROM 	Project AS P
		JOIN Employee AS E
		ON P.employee_id = E.employee_id
GROUP BY	project_id

-- @lc code=end

