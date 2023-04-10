--
-- @lc app=leetcode.cn id=613 lang=mysql
--
-- [613] 直线上的最近距离
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  MIN(ABS(P1.x - P2.x)) AS `shortest`
FROM    point P1, point P2
WHERE   P1.x < P2.x -- 避免自连接时的重复计算
-- @lc code=end

