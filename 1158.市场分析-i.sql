--
-- @lc app=leetcode.cn id=1158 lang=mysql
--
-- [1158] 市场分析 I
--

-- @lc code=start
# Write your MySQL query statement below
select user_id as buyer_id, join_date, ifnull(orders_in_2019,0) as orders_in_2019
from Users u
left join(  select count(*) as orders_in_2019, buyer_id
            from Orders o
            where o.order_date like '2019%'
            group by buyer_id
        ) as t on u.user_id = t.buyer_id

-- @lc code=end

