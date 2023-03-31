--
-- @lc app=leetcode.cn id=1783 lang=mysql
--
-- [1783] 大满贯数量
--

-- @lc code=start
# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT p.player_id, p.player_name, SUM(p.player_id = c.Wimbledon) + SUM(p.player_id = c.Fr_open) + SUM(p.player_id = c.US_open) + SUM(p.player_id = c.Au_open) grand_slams_count 
FROM Championships c, Players p
GROUP BY p.player_id
HAVING grand_slams_count > 0
-- @lc code=end

