--
-- @lc app=leetcode.cn id=603 lang=mysql
--
-- [603] 连续空余座位
--

-- @lc code=start
# Write your MySQL query statement below
select c1.seat_id # , c1.free, c2.free as free_before, c3.free as free_after
from Cinema c1
left join Cinema c2 on c2.seat_id = c1.seat_id - 1
left join Cinema c3 on c3.seat_id = c1.seat_id + 1
where c1.free = 1 
and (c2.free = 1 or c3.free = 1)
order by c1.seat_id
-- @lc code=end
