--
-- @lc app=leetcode.cn id=1934 lang=mysql
--
-- [1934] 确认率
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	S.user_id, 
		IFNULL(confirmation_rate, 0.00) AS confirmation_rate
FROM 	Signups AS S
		LEFT JOIN 	
			(SELECT	user_id, 
					ROUND(
						COUNT(
							CASE WHEN action = 'confirmed' THEN 1 
							ELSE NULL 
						END)/COUNT(*), 
						2) AS `confirmation_rate`
			FROM 	Confirmations 
			GROUP BY	user_id) AS R
		ON S.user_id = R.user_id

/* 大神的代码：直接拼接后计算 */
SELECT
	s.user_id,
	ifnull( round( sum( action = 'confirmed' ) / count( c.action ), 2 ), 0.00 ) AS confirmation_rate 
FROM
	signups AS s
	LEFT JOIN confirmations AS c ON s.user_id = c.user_id 
GROUP BY
	s.user_id
-- @lc code=end

