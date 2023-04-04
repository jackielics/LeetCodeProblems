--
-- @lc app=leetcode.cn id=1308 lang=mysql
--
-- [1308] 不同性别每日分数总计
--

-- @lc code=start
# Write your MySQL query statement below

select s1.gender, 
    s1.day, 
    (select sum(s2.score_points)
        from Scores s2
        where s2.day <= s1.day and s2.gender = s1.gender
    ) as total
from Scores s1
group by s1.day, s1.gender
order by s1.gender, s1.day

-- @lc code=end

