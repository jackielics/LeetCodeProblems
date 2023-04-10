--
-- @lc app=leetcode.cn id=579 lang=mysql
--
-- [579] 查询员工的累计薪水
--
-- @lc code=start
# Write your MySQL query statement below

/* 参考大神的解法 */
SELECT  id, 
        `month`, 
        Salary
FROM 
    (SELECT  id,
            `month`,
            SUM(salary) OVER (
                PARTITION BY id
                ORDER BY
                    month 
                    -- RANGE：当前月份逻辑上的前两个月，表中存在则计算不存在则忽略
                    -- ROWS：当前月份、表中存在、距离最近的先前两个月
                    
                    /* RANGE BETWEEN 2 PRECEDING AND CURRENT ROW */
                    RANGE 2 PRECEDING
            ) AS Salary, 
            ROW_NUMBER() OVER (
                PARTITION BY id
                ORDER BY
                    month DESC
            ) AS `rn`
    FROM    Employee ) AS `T`
WHERE   `rn` > 1
ORDER BY
    id,
    month DESC 

/* SELECT Id, Month, Salary
FROM (
    SELECT Id, Month, 
    SUM(Salary) OVER (PARTITION BY Id ORDER BY Month asc range 2 PRECEDING) AS Salary, 
    rank() OVER (PARTITION BY Id ORDER BY Month DESC) AS r
      FROM Employee
    ) t
WHERE r > 1
ORDER BY Id, Month DESC; */

-- @lc code=end