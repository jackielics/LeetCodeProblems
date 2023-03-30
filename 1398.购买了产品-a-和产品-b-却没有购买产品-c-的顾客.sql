--
-- @lc app=leetcode.cn id=1398 lang=mysql
--
-- [1398] 购买了产品 A 和产品 B 却没有购买产品 C 的顾客
--

-- @lc code=start
# Write your MySQL query statement below
select o.customer_id as customer_id, 
(select customer_name from Customers c where c.customer_id = o.customer_id) as customer_name 
from Orders o
group by o.customer_id
having SUM(o.product_name = 'A') > 0
    and SUM(o.product_name = 'B') > 0
    and SUM(o.product_name = 'C') = 0
order by o.customer_id asc
-- @lc code=end

