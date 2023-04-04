--
-- @lc app=leetcode.cn id=1321 lang=mysql
--
-- [1321] 餐馆营业额变化增长
--

-- @lc code=start
# Write your MySQL query statement below
select distinct o1.visited_on as visited_on,
    @sum := (
        select sum(o2.amount) from Customer o2 where o2.visited_on between subdate(o1.visited_on, 6) and o1.visited_on
    ) as amount, 
    round(@sum / 7, 2) as average_amount 
from Customer o1 
where exists ( 
    select * 
    from Customer o2 
    where o2.visited_on <= subdate(o1.visited_on, 6) 
)
order by o1.visited_on asc
-- @lc code=end

