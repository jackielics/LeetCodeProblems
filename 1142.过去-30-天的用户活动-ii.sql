--
-- @lc app=leetcode.cn id=1142 lang=mysql
--
-- [1142] 过去30天的用户活动 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	ROUND(IFNULL(SUM(frequency) / COUNT(user_id), 0), 2) AS average_sessions_per_user
FROM 
(SELECT 	user_id, 
		COUNT(DISTINCT session_id) AS frequency
FROM 	Activity
WHERE	activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY 	user_id) AS T

/* 大神的解法：深入理解了COUNT和DISTINCT */
SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0) AS average_sessions_per_user
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30
-- @lc code=end

