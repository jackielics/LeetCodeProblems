--
-- @lc app=leetcode.cn id=1445 lang=mysql
--
-- [1445] 苹果和桔子
--

-- @lc code=start
# Write your MySQL query statement below
select sale_date, sum(if(fruit='apples', sold_num, -sold_num)) as diff
from Sales
group by sale_date
order by sale_date
-- @lc code=end

