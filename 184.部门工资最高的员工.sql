--
-- @lc app=leetcode.cn id=184 lang=mysql
--
-- [184] 部门工资最高的员工
--

-- @lc code=start
# Write your MySQL query statement below
/* select d.name as Department, 
    e.name as Employee, 
    e.salary as Salary
from (
    select e2.departmentId as departmentId, max(e2.salary) as max_salary
    from Employee e2, 
    where e2.departmentId = e.departmentId
    group by e2.departmentId
) as m
right join Employee as e
on e.departmentId = m.departmentId
    and e.salary = m.max_salary
left join Department d on d.Id = m.departmentId */
/* 其实没有那么难，只是当时的自己思路局限了而已 */
select d.name as Department, 
    e.name as Employee, 
    e.salary as Salary
from Employee e
left join Department d
on e.departmentId = d.Id
where (e.departmentId, e.salary) in (
    select e2.departmentId, max(e2.salary)
    from Employee e2
    group by e2.departmentId
)


-- @lc code=end

