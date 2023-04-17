--
-- @lc app=leetcode.cn id=1132 lang=mysql
--
-- [1132] 报告的记录 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	ROUND(AVG(spam_rate), 2) AS average_daily_percent
FROM		
(SELECT	action_date, 
		# 一天的移除率 = 一天的移除数 / 一天的总数 * 100
		# 不加distinct会出错，因为一天可能有多个垃圾邮件
		COUNT(DISTINCT R.post_id) / COUNT(DISTINCT A.post_id) * 100 AS 'spam_rate'
FROM 	Actions A
		LEFT JOIN 	Removals R
		# 不能用USING替代
		ON A.post_id = R.post_id
WHERE 	extra = 'spam' # 筛选出每天的垃圾邮件
GROUP BY	action_date) T1

/* 先算一天的移除率，再除以天数算平均 */
-- @lc code=end

