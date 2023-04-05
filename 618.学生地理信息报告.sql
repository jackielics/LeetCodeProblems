--
-- @lc app=leetcode.cn id=618 lang=mysql
--
-- [618] 学生地理信息报告
--

-- @lc code=start
# Write your MySQL query statement below
/* 参考大神：https://leetcode.cn/problems/students-report-by-geography/solution/zong-jie-ge-lei-biao-ge-ge-shi-hua-wen-t-tl4e/ */
SELECT  
    MAX(CASE continent WHEN 'America' THEN NAME ELSE NULL END) AS America,
    MAX(CASE continent WHEN 'Asia' THEN NAME ELSE NULL END) AS Asia,
    MAX(CASE continent WHEN 'Europe' THEN NAME ELSE NULL END) AS Europe 
FROM
    (SELECT name, 
            continent, 
            -- 存在同大洲同名者，用ROW_NUMBER更保险
            ROW_NUMBER() OVER (
                PARTITION BY continent
                ORDER BY name 
            ) AS `rk`
    FROM    Student ) AS `T`
GROUP BY    rk

-- @lc code=end

