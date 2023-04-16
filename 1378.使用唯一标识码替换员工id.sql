--
-- @lc app=leetcode.cn id=1378 lang=mysql
--
-- [1378] 使用唯一标识码替换员工ID
--

-- @lc code=start
# Write your MySQL query statement below
	SELECT 	unique_id, 
			name
	FROM 	Employees EM
			LEFT JOIN	EmployeeUNI EI
			ON	EM.id = EI.id
-- @lc code=end

