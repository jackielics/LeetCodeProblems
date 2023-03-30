--
-- @lc app=leetcode.cn id=1587 lang=mysql
--
-- [1587] 银行账户概要 II
--

-- @lc code=start
# Write your MySQL query statement below
select  name, sum(amount) as balance
from Transactions t
left join Users u ON t.account = u.account
group by t.account
having sum(amount)>10000
-- @lc code=end

