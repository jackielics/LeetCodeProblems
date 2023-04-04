--
-- @lc app=leetcode.cn id=1867 lang=mysql
--
-- [1867] 最大数量高于平均水平的订单
--

-- @lc code=start
# Write your MySQL query statement below
select distinct order_id
from OrdersDetails o2
group by order_id
having max(quantity) > (
    select max(ave)
    from (select order_id, (sum(quantity) / count(*)) as 'ave'
            from OrdersDetails o1
            group by order_id) as OrdersAverage
)

/* (select order_id, (sum(quantity) / count(*)) as 'ave'
from OrdersDetails o1
group by order_id) as OrdersAverage */
-- @lc code=end

