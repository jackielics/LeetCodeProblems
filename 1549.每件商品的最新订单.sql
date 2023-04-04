--
-- @lc app=leetcode.cn id=1549 lang=mysql
--
-- [1549] 每件商品的最新订单
--

-- @lc code=start
# Write your MySQL query statement below
select p.product_name, o1.product_id, o1.order_id, o1.order_date
from Orders o1
left join Products p
on o1.product_id  = p.product_id
where o1.order_date = (
    select max(o2.order_date)
    from Orders o2
    where o2.product_id = o1.product_id
)
order by product_name asc, product_id asc, order_id asc
-- @lc code=end

