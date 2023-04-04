--
-- @lc app=leetcode.cn id=181 lang=mysql
--
-- [181] 超过经理收入的员工
--

-- @lc code=start
# Write your MySQL query statement below
select e.name as Employee
from Employee e
where e.Salary > (select Salary 
                    from Employee 
                    where Id = e.ManagerId)
-- @lc code=end

