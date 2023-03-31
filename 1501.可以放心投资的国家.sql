--
-- @lc app=leetcode.cn id=1501 lang=mysql
--
-- [1501] 可以放心投资的国家
--

-- @lc code=start
# Write your MySQL query statement below
select country_name as country # , count(*)  , avg(duration), (select avg(c1.duration) from Calls c1)
from (select co.country_name, ca1.duration
        from (select id, co.name as country_name
                from Person p, Country co
                where left(p.phone_number, 3) = co.country_code
                ) as co
        right join Calls ca1 on ca1.caller_id = co.id
        union all
        select co.country_name, ca1.duration
        from (select id, co.name as country_name
                from Person p, Country co
                where left(p.phone_number, 3) = co.country_code
                ) as co
        right join Calls ca1 on ca1.callee_id = co.id) as d
group by country_name
having avg(duration) > (select avg(c1.duration) from Calls c1)
-- @lc code=end

