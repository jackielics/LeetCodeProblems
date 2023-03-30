--

-- @lc app=leetcode.cn id=1211 lang=mysql

--

-- [1211] 查询结果的质量和占比

--

-- @lc code=start

# Write your MySQL query statement below
select
    query_name,
    round(sum(rating / position) / count(*), 2) as quality,
    round(
        sum(if(rating < 3, 1, 0)) / count(*) * 100,
        2
    ) as poor_query_percentage
from Queries
group by query_name 
-- @lc code=end