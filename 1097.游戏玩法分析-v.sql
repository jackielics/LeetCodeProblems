--
-- @lc app=leetcode.cn id=1097 lang=mysql
--
-- [1097] 游戏玩法分析 V
--

-- @lc code=start
# Write your MySQL query statement below

# 找出所有安装日期
SELECT 	DISTINCT	MIN(event_date) AS install_date, 
					player_id, 
					SUM(
						CASE
							WHEN	event_date = MIN(event_date) + 1 THEN 1
							ELSE 0 
						END
					) AS install_count
FROM	Activity
GROUP BY	player_id
#下一步是检查每个玩家的安装日期后的下一天是否有登录
-- @lc code=end

