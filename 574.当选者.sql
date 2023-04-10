--
-- @lc app=leetcode.cn id=574 lang=mysql
--
-- [574] 当选者
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  name
FROM 
    (SELECT  name, 
            ROW_NUMBER() OVER(ORDER BY `poll` DESC) AS `rk`
    FROM    -- 计算得票数
        (SELECT  candidateId, 
                COUNT(id) AS `poll`
        FROM    Vote 
        GROUP BY candidateId ) AS `T`
        LEFT JOIN   Candidate AS `C`
        ON  T.candidateId = C.id) AS `T2`
WHERE   `rk` = 1

/* 大神的方法：用ORDER BY + LIMIT减少了一次嵌套 */

select Name
from (
  select CandidateId as id
  from Vote
  group by CandidateId
  order by count(id) desc
  limit 1
) as Winner join Candidate
on Winner.id = Candidate.id
-- @lc code=end

