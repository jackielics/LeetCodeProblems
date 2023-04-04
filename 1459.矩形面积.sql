--
-- @lc app=leetcode.cn id=1459 lang=mysql
--
-- [1459] 矩形面积
--

-- @lc code=start
# Write your MySQL query statement below
select p1.id as p1, 
    p2.id as p2, 
    abs((p1.x_value - p2.x_value) * (p1.y_value - p2.y_value)) as area
from Points p1, Points p2
where p1.id < p2.id 
    and p1.x_value <> p2.x_value
    and p1.y_value <> p2.y_value
order by area desc, p1 asc, p2 asc
-- @lc code=end

