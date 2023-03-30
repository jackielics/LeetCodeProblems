--
-- @lc app=leetcode.cn id=1741 lang=mysql
--
-- [1741] 查找每个员工花费的总时间
--

-- @lc code=start
# Write your MySQL query statement below
select event_day as day, emp_id, sum(out_time-in_time) as total_time
from Employees 
group by event_day,emp_id
-- @lc code=end

