--
-- @lc app=leetcode.cn id=570 lang=mysql
--
-- [570] 至少有5名直接下属的经理
--

-- @lc code=start
# Write your MySQL query statement below

/* select (select e2.name
    from Employee e2 
    where e2.id = e1.managerId) as name 
from Employee e1
where exists(select * 
    from Employee e3
    where e3.managerId = e1.managerId)
group by e1.managerId 
having count(*) >= 5  */

select name
from (select e1.managerId as managerId, e2.name as name
        from Employee e1
        left join Employee e2 on e1.managerId = e2.id) as m
where name is not null
group by name
having count(*) >= 5

/* select e1.managerId, e2.name
        from Employee e1
        left join Employee e2 on e1.managerId = e2.id */
-- @lc code=end

