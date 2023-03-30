--
-- @lc app=leetcode.cn id=1393 lang=mysql
--
-- [1393] 股票的资本损益
--

-- @lc code=start
# Write your MySQL query statement below
select stock_name, sum(
    case
        when operation = 'buy' then -price
        when operation = 'sell' then price
    end
) as capital_gain_loss 
from Stocks
group by stock_name
-- @lc code=end

