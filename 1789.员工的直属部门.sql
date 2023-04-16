--
-- @lc app=leetcode.cn id=1789 lang=mysql
--
-- [1789] 员工的直属部门
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	employee_id, 
		IF(	COUNT(department_id)=1, 
			department_id, 
			MAX(
				CASE
					WHEN primary_flag = 'Y' THEN department_id
					ELSE NULL
				END)) AS department_id
FROM 	Employee 
GROUP BY 	employee_id


-- @lc code=end

