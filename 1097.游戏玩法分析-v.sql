--
-- @lc app=leetcode.cn id=1097 lang=mysql
--
-- [1097] 游戏玩法分析 V
--

-- @lc code=start
# Write your MySQL query statement below

# 找出所有安装日期

SELECT 	DISTINCT	install_dt, 
					count(DISTINCT player_id) AS installs, 
					ROUND(
						SUM(
							CASE
								WHEN event_date = DATE_ADD(install_dt, INTERVAL 1 DAY) THEN 1
								ELSE 0
							END
						) / count(DISTINCT player_id)
						, 2) AS Day1_retention
FROM
	(SELECT 	player_id, 
			event_date, 
			MIN(event_date) OVER(PARTITION BY player_id) AS install_dt # 该玩家的安装日期
			COUNT() OVER(PARTITION BY event_date)  # 该日期的活跃玩家数(不可误当做该日期安装数)
	FROM 	Activity A1) AS T
GROUP BY 	install_dt


-- @lc code=end

