--
-- @lc app=leetcode.cn id=1407 lang=mysql
--
-- [1407] 排名靠前的旅行者
--

-- @lc code=start
# Write your MySQL query statement below
/* select (select name
        from Users 
        where Users.id = Rides.user_id) as name, 
        sum(distance) as travelled_distance 
from Rides
group by user_id
order by travelled_distance desc, name asc */
select u.name as name, ifnull(d.travelled_distance, 0) as travelled_distance
from Users u
left join ( select user_id, sum(distance) as travelled_distance
            from Rides
            group by user_id
) as d on u.id = d.user_id
order by travelled_distance desc, name asc
-- @lc code=end

