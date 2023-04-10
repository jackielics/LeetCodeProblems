--
-- @lc app=leetcode.cn id=602 lang=mysql
--
-- [602] 好友申请 II ：谁有最多的好友
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  `user` AS `id`, 
        COUNT(*) AS `num`
FROM    
    (SELECT  requester_id AS `user`,   
            accepter_id AS `friend`
    FROM    RequestAccepted 
    UNION 
    SELECT  accepter_id AS `user`,   
            requester_id AS `friend`
    FROM    RequestAccepted) AS `T`
GROUP BY    `user`
ORDER BY    `num` DESC
LIMIT 1

/* 大神的方法：更简洁，仅计算被人当好友的次数即可 */
select id, count(*) as num
from (
    select requester_id as id from RequestAccepted
    union all
    select accepter_id from RequestAccepted
) as A
group by id
order by count(*) desc
limit 1
-- @lc code=end

