--

-- @lc app=leetcode.cn id=1633 lang=mysql

--

-- [1633] 各赛事的用户注册率

--

-- @lc code=start

# Write your MySQL query statement below
select contest_id, round(count(*) / (select count(*) from Users) * 100, 2) as percentage
from Register
group by contest_id
order by
    percentage desc, 
    contest_id asc 
-- @lc code=end