--
-- @lc app=leetcode.cn id=1731 lang=mysql
--
-- [1731] 每位经理的下属员工数量
--

-- @lc code=start
# Write your MySQL query statement below
select reports_to as employee_id, 
    (   select name 
        from Employees e2
        where e2.employee_id = e1.reports_to
        ) as name, 
    count(*) as reports_count, 
    round(avg(age)) as average_age
from Employees e1
where reports_to is not null
group by reports_to
order by employee_id
-- @lc code=end

