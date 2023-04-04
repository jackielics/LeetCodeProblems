--
-- @lc app=leetcode.cn id=1077 lang=mysql
--
-- [1077] 项目员工 III
--

-- @lc code=start
# Write your MySQL query statement below
select p.project_id as project_id, e.employee_id as employee_id
from Project p
left join Employee e
on p.employee_id = e.employee_id
where e.experience_years = (
    select max(e1.experience_years)
    from Project p1
    left join Employee e1
    on p1.employee_id = e1.employee_id
    where p1.project_id = p.project_id
)
-- @lc code=end

