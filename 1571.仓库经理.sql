--
-- @lc app=leetcode.cn id=1571 lang=mysql
--
-- [1571] 仓库经理
--

-- @lc code=start
# Write your MySQL query statement below
select name as WAREHOUSE_NAME, 
        sum(units * Width * Length * Height)  as VOLUME
from Warehouse w
left join Products p
on w.product_id = p.product_id
group by name
-- @lc code=end

