--
-- @lc app=leetcode.cn id=262 lang=mysql
--
-- [262] 行程和用户
--

-- @lc code=start
# Write your MySQL query statement below
select request_at as 'Day', 
    round((select count(*)
        from (select *
        from Trips t2
        where not exists(
            select * 
            from Users u
            where u.banned = 'Yes' and (u.users_id = t2.client_id or u.users_id = t2.driver_id)
        ) and t2.status <> 'completed' and t2.request_at = t1.request_at) as p)
        / count(*), 2) as 'Cancellation Rate'
from Trips t1
WHERE t1.request_at between '2013-10-01' and '2013-10-03'
and 'No' = (
    SELECT u.banned FROM Users u WHERE u.users_id = t1.client_id
) AND 'No' = (
    SELECT u.banned FROM Users u WHERE u.users_id = t1.driver_id
)
group by t1.request_at
-- @lc code=end

