--
-- @lc app=leetcode.cn id=1113 lang=mysql
--
-- [1113] 报告的记录
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	extra AS report_reason, 
		COUNT(DISTINCT post_id) AS report_count
FROM	Actions 
WHERE	action_date = SUBDATE('2019-07-05', INTERVAL 1 DAY)
		AND action = 'report'
GROUP BY	extra
	
-- @lc code=end

