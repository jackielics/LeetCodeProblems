--
-- @lc app=leetcode.cn id=1127 lang=mysql
--
-- [1127] 用户购买平台
--

-- @lc code=start
# Write your MySQL query statement below
/* 大神的方法：笛卡尔积连接 */
SELECT	spend_date, 
		B.platform, # 不要写成A.platform
		SUM(IF(A.platform = B.platform, amount, 0)) AS total_amount, 
		COUNT(IF(A.platform=B.platform, 1, null)) AS total_users
FROM 
	(SELECT spend_date, 
			user_id, 
			IF(COUNT(DISTINCT platform) = 2, 'both', platform) AS platform, 
			SUM(amount) AS amount
	FROM 	Spending 
	GROUP BY	user_id, 
				spend_date) AS A,
	(
		SELECT	'desktop' AS platform UNION
		SELECT	'mobile' AS platform UNION
		SELECT	'both' AS platform
	) AS B
GROUP BY	spend_date, 
			platform
-- @lc code=end

