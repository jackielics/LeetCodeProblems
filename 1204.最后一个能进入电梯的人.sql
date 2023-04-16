--
-- @lc app=leetcode.cn id=1204 lang=mysql
--
-- [1204] 最后一个能进入电梯的人
--

-- @lc code=start
# Write your MySQL query statement below
/* WITH Q AS
(SELECT 	person_name, 
			weight, 
			turn, 
			SUM(weight) OVER(ORDER BY turn ASC) AS sum_weight
	FROM 	Queue)

SELECT	person_name
FROM 	Q
WHERE	turn = (SELECT MAX(turn) 
					FROM Q 
					WHERE sum_weight <= 1000) */

/* 大神的方法：计算累计，一对多拼接自身算聚合函数 */

SELECT a.person_name
FROM Queue a, Queue b
WHERE a.turn >= b.turn
GROUP BY a.person_id HAVING SUM(b.weight) <= 1000
ORDER BY a.turn DESC
LIMIT 1
-- @lc code=end

