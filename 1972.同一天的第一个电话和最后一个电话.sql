--
-- @lc app=leetcode.cn id=1972 lang=mysql
--
-- [1972] 同一天的第一个电话和最后一个电话
--

-- @lc code=start
# Write your MySQL query statement below
WITH UserCall AS
(SELECT  caller_id AS 'user_a', 
        recipient_id AS 'user_b', 
        call_time
FROM    Calls 
UNION
SELECT  recipient_id, 
        caller_id, 
        call_time
FROM    Calls ), 
FirstLastCall AS
(SELECT  user_a, 
        MIN(call_time) AS 'first_call', 
        (
            SELECT      u2.user_b
            FROM        UserCall u2
            WHERE       u2.user_a = u1.user_a
                        AND u2.call_time = MIN(u1.call_time)
        ) AS 'first_to', 
        MAX(call_time) AS 'last_call', 
        (
            SELECT      u2.user_b
            FROM        UserCall u2
            WHERE       u2.user_a = u1.user_a
                        AND u2.call_time = MAX(u1.call_time)
        ) AS 'last_to'
FROM    UserCall u1
GROUP BY    user_a, 
            DATE_FORMAT(call_time, '%Y-%m-%d'))

SELECT  DISTINCT user_a AS 'user_id'
FROM    FirstLastCall
WHERE   first_to = last_to

/* 大神的代码：能用窗口函数就不要用GROUP BY */
with a as (
    SELECT caller_id, recipient_id, call_time
    FROM Calls
    UNION ALL
    SELECT recipient_id caller_id, caller_id recipient_id, call_time
    FROM Calls
)

SELECT DISTINCT a.caller_id user_id
FROM
(SELECT caller_id, recipient_id, dense_rank() over (PARTITION BY caller_id, DATE_FORMAT(call_time, '%Y-%m-%d') order by call_time) AS rk
FROM a) a
INNER JOIN 
(SELECT caller_id, recipient_id, dense_rank() over (PARTITION BY caller_id, DATE_FORMAT(call_time, '%Y-%m-%d') order by call_time DESC) AS rk
FROM a) b
ON a.caller_id = b.caller_id AND a.recipient_id = b.recipient_id AND a.rk = 1 AND b.rk = 1

-- @lc code=end

