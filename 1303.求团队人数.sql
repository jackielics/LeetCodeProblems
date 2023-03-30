--
-- @lc app=leetcode.cn id=1303 lang=mysql
--
-- [1303] 求团队人数
--

-- @lc code=start
# Write your MySQL query statement below
select e1.employee_id as employee_id, t.team_size as team_size
from Employee e1, (
    select e2.team_id as team_id, count(*) as team_size
    from Employee e2
    group by e2.team_id
) as t
where e1.team_id = t.team_id

-- @lc code=end

