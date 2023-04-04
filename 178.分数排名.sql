--
-- @lc app=leetcode.cn id=178 lang=mysql
--
-- [178] 分数排名
--

-- @lc code=start
# Write your MySQL query statement below

/* 用了RANK()，事半功倍 */
select s1.score, 
    trk.rk as 'rank'
from Scores s1
left join ( select score,
                rank() over(order by score desc) as 'rk'
            from Scores s
            group by score) as trk
on s1.score = trk.score
order by s1.score desc

/* 大神的方法：同表拼接实现排名 */
/* SELECT a.Score, COUNT(DISTINCT b.Score) AS `RANK`
FROM Scores a, Scores b
WHERE a.Score <= b.Score
GROUP BY a.Id
ORDER BY `RANK`; */
-- @lc code=end

