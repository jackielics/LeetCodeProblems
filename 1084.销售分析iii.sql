--
-- @lc app=leetcode.cn id=1084 lang=mysql
--
-- [1084] 销售分析III
--

-- @lc code=start
# Write your MySQL query statement below
select s.product_id as product_id, (select product_name from Product p where p.product_id = s.product_id) as product_name
from Sales s
group by s.product_id
having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31'
-- @lc code=end

