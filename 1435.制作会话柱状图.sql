--
-- @lc app=leetcode.cn id=1435 lang=mysql
--
-- [1435] 制作会话柱状图
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	"[0-5>" AS `bin`, 
		SUM(duration >= 0 AND duration < 5 * 60) AS `total`
FROM	Sessions
UNION ALL
SELECT	"[5-10>" AS `bin`, 
		SUM(duration >= 5 * 60 AND duration < 10 * 60) AS `total`
FROM	Sessions
UNION ALL
SELECT	"[10-15>" AS `bin`, 
		SUM(duration >= 10 * 60 AND duration < 15 * 60) AS `total`
FROM	Sessions
UNION ALL
SELECT	"15 or more" AS `bin`, 
		SUM(duration >= 15 * 60) AS `total`
FROM	Sessions
-- @lc code=end

