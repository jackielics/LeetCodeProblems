--
-- @lc app=leetcode.cn id=1251 lang=mysql
--
-- [1251] 平均售价
--

-- @lc code=start
# Write your MySQL query statement below
/* 编写SQL查询以查找每种产品的平均售价。
average_price 应该四舍五入到小数点后两位 */
select u.product_id as product_id, 
    round(sum(u.units * p.price) / sum(u.units), 2) as average_price 
from Prices p, UnitsSold u
where p.product_id = u.product_id 
    and u.purchase_date between p.start_date and p.end_date
group by u.product_id

-- @lc code=end

