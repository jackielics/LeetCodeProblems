--
-- @lc app=leetcode.cn id=569 lang=mysql
--
-- [569] 员工薪水中位数
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  id, 
        company, 
        salary
FROM    
(SELECT  id, 
        company, 
        salary, 
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary) AS `rk`,
        COUNT(*) OVER (PARTITION BY company) AS `cnt`
FROM    Employee ) AS `subquery`
WHERE   `rk` IN (FLOOR(`cnt` / 2 + 0.5), CEIL(`cnt` / 2 + 0.5))

-- @lc code=end

