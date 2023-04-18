--
-- @lc app=leetcode.cn id=1107 lang=mysql
--
-- [1107] 每日新用户统计
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	first_activity_date AS login_date, 
		COUNT(DISTINCT user_id) AS user_count
FROM 
	(SELECT	user_id,
			activity,
			activity_date,
			MIN(activity_date) OVER(PARTITION BY user_id) AS first_activity_date
	FROM	Traffic
	WHERE 	activity = 'login') AS T
WHERE	DATEDIFF('2019-06-30', activity_date) <= 90
		AND	activity_date = first_activity_date
GROUP BY	first_activity_date

/* DATEDIFF('2019-06-30', activity_date) <= 90 */
-- @lc code=end

