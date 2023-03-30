--
-- @lc app=leetcode.cn id=586 lang=mysql
--
-- [586] 订单最多的客户
--

-- @lc code=start
# Write your MySQL query statement below
select customer_number 
from Orders
GROUP BY customer_number
having count(*) = (
    select max(count) 
    from (
        select count(*) as count 
        from Orders 
        group by customer_number
        ) as t
    )
-- @lc code=end

