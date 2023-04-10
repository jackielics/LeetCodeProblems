--
-- @lc app=leetcode.cn id=512 lang=mysql
--
-- [512] 游戏玩法分析 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  player_id, 
        device_id
FROM    
(SELECT  player_id, 
        device_id, 
        event_date, 
        RANK() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS `rk`
FROM    Activity) AS `T`
WHERE   rk = 1

-- @lc code=end

