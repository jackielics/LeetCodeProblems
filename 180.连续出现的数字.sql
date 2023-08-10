--
-- @lc app=leetcode.cn id=180 lang=mysql
--
-- [180] 连续出现的数字
--

-- @lc code=start
# Write your MySQL query statement below
select distinct l2.Num as ConsecutiveNums # 'select distinct'
from Logs l1, Logs l2, Logs l3
where l1.Num = l2.Num 
    and l2.Num = l3.Num
    and l1.Id = l2.Id - 1 
    and l2.Id = l3.Id - 1;
# 
-- @lc code=end

