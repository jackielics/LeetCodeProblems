--
-- @lc app=leetcode.cn id=585 lang=mysql
--
-- [585] 2016年的投资
--

-- @lc code=start
# Write your MySQL query statement below
/* 15年投资不独特，经纬度独特 */

SELECT  ROUND(SUM(TIV_2016), 2) AS `TIV_2016`
FROM    
(SELECT COUNT(1) OVER (
            PARTITION BY TIV_2015
        ) AS `cnt_15`, 
        TIV_2016, 
        COUNT(1) OVER (
            PARTITION BY LAT, LON
        ) AS `cnt_l`
FROM    insurance ) AS `T`
WHERE   cnt_15 > 1
        AND cnt_l = 1

-- @lc code=end

