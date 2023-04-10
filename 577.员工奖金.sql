--
-- @lc app=leetcode.cn id=577 lang=mysql
--
-- [577] 员工奖金
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  name, 
        bonus
FROM    Employee AS `E`
        LEFT JOIN   Bonus AS `B`
        ON  E.empId = B.empId
WHERE   bonus IS NULL
        OR bonus < 1000
-- @lc code=end

