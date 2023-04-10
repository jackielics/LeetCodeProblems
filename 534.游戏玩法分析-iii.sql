--
-- @lc app=leetcode.cn id=534 lang=mysql
--
-- [534] 游戏玩法分析 III
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  player_id, 
        event_date, 
        SUM(games_played) OVER(PARTITION BY player_id ORDER BY event_date ASC) AS `games_played_so_far`
FROM    Activity 
-- @lc code=end

