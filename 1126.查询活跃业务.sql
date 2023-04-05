--
-- @lc app=leetcode.cn id=1126 lang=mysql
--
-- [1126] 查询活跃业务
--

-- @lc code=start
# Write your MySQL query statement below

WITH tmp AS
(
	SELECT  event_type
	       ,SUM(occurences)/COUNT(*) AS avg_event
	FROM Events
	GROUP BY  event_type
) 

SELECT e.business_id
FROM Events AS e
LEFT JOIN tmp
ON e.event_type = tmp.event_type
WHERE e.occurences > tmp.avg_event
GROUP BY e.business_id 
HAVING COUNT(*) >= 2

-- @lc code=end

