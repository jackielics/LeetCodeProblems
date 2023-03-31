--
-- @lc app=leetcode.cn id=626 lang=mysql
--
-- [626] 换座位
--

-- @lc code=start
# Write your MySQL query statement below
select (
    case 
        when id%2=0 then id-1
        when id%2=1 and id<>(select max(s1.id) from Seat s1) then id+1
        else id
    end
) as id, student
from Seat
order by id


-- @lc code=end

