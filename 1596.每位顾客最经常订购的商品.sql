--
-- @lc app=leetcode.cn id=1596 lang=mysql
--
-- [1596] 每位顾客最经常订购的商品
--

-- @lc code=start
# Write your MySQL query statement below
select  o.customer_id, 
        o.product_id, 
    (   select p1.product_name 
        from Products p1
        where p1.product_id = o.product_id
        ) as product_name
from Orders o
left join Products p
on o.product_id = p.product_id
group by o.customer_id, o.product_id
having count(*) = (
    select max(t.cnt)
    from (  select count(*) as cnt
            from    Orders o1
            where  o1.customer_id = o.customer_id
            group by o1.product_id
            ) as t
)
-- @lc code=end

