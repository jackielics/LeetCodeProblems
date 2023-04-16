--
-- @lc app=leetcode.cn id=1350 lang=mysql
--
-- [1350] 院系无效的学生
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	S.id, 
		S.name
FROM 	Students S
		LEFT JOIN 	Departments D
		ON 	S.department_id = D.id
WHERE 	D.id IS NULL	
-- @lc code=end

