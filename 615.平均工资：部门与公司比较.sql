--
-- @lc app=leetcode.cn id=615 lang=mysql
--
-- [615] 平均工资：部门与公司比较
--

-- @lc code=start
# Write your MySQL query statement below

SELECT  LEFT(pay_date, 7) AS `pay_month`, 
        department_id, 
        (
            CASE 
                WHEN ROUND(AVG(amount),2) > ROUND(@var := (SELECT  AVG(s2.amount)
                                            FROM    salary s2
                                            WHERE   LEFT(s2.pay_date, 7) = LEFT(s1.pay_date, 7)
                                            ),2) THEN 'higher'
                WHEN ROUND(AVG(amount),2) < ROUND((SELECT  AVG(s2.amount)
                                            FROM    salary s2
                                            WHERE   LEFT(s2.pay_date, 7) = LEFT(s1.pay_date, 7)
                                            ),2) THEN 'lower'
                ELSE 'same'
            END 
        ) AS `comparison`
FROM    salary s1
        LEFT JOIN employee 
        USING (employee_id )
GROUP BY    LEFT(pay_date, 7), 
            department_id
-- @lc code=end

