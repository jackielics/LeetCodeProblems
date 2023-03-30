--
-- @lc app=leetcode.cn id=1699 lang=mysql
--
-- [1699] 两人之间的通话次数
--

-- @lc code=start
# Write your MySQL query statement below
select 
    person1, person2, count(*) as call_count, sum(duration) as total_duration
from (
    select 
        if(from_id<to_id, from_id, to_id) as person1,
        if(from_id<to_id, to_id, from_id) as person2,
        duration
    from Calls
) as c
group by person1, person2

-- @lc code=end

