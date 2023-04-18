--
-- @lc app=leetcode.cn id=1149 lang=mysql
--
-- [1149] 文章浏览 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	DISTINCT viewer_id AS id
FROM	Views 
GROUP BY	viewer_id, 
			view_date
HAVING	COUNT(DISTINCT article_id) >= 2
-- @lc code=end

