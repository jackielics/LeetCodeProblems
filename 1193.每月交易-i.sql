--
-- @lc app=leetcode.cn id=1193 lang=mysql
--
-- [1193] 每月交易 I
--

-- @lc code=start
# Write your MySQL query statement below
select LEFT(trans_date, 7) as month, 
    country, count(*) as trans_count, 
    sum(if(state = 'approved', 1, 0)) as approved_count, 
    sum(amount) as trans_total_amount, 
    sum(if(state = 'approved', amount, 0)) as approved_total_amount
from Transactions
group by LEFT(trans_date, 7), country

-- @lc code=end

