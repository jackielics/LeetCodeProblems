--
-- @lc app=leetcode.cn id=1270 lang=mysql
--
-- [1270] 向公司CEO汇报工作的所有人
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT E1.employee_id
FROM    Employees E1
        LEFT JOIN   Employees E2
        ON  E1.manager_id = E2.employee_id
        LEFT JOIN   Employees E3
        ON  E2.manager_id = E3.employee_id
WHERE   E1.employee_id <> 1
        AND 1 IN (E1.manager_id, E2.manager_id, E3.manager_id)
-- @lc code=end

