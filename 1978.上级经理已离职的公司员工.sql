--
-- @lc app=leetcode.cn id=1978 lang=mysql
--
-- [1978] 上级经理已离职的公司员工
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	employee_id 
FROM 	Employees E1
WHERE 	salary < 30000
		AND manager_id IS NOT NULL
		AND NOT EXISTS (
			SELECT 	1
			FROM 	Employees E2
			WHERE	E2.employee_id = E1.manager_id
		)
ORDER BY	employee_id ASC

/* 大神的解法：用in避开判断空值的情形 */
select employee_id
from Employees
where salary < 30000
and manager_id not in (select distinct employee_id from Employees)
order by employee_id
-- @lc code=end

