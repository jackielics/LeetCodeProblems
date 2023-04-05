--
-- @lc app=leetcode.cn id=185 lang=mysql
--
-- [185] 部门工资前三高的所有员工
--

-- @lc code=start
# Write your MySQL query statement below
/* 用到了窗口函数，本身就比较简洁了 */
SELECT  Department, 
        Employee, 
        Salary 
FROM 
    (SELECT  d.name AS `Department`, 
            e.name AS `Employee`, 
            salary AS `Salary`, 
            DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS `rk`
    FROM    Employee e
            LEFT JOIN Department d
            ON d.id = e.departmentId) AS t
WHERE rk <= 3

-- @lc code=end

