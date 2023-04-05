--
-- @lc app=leetcode.cn id=1225 lang=mysql
--
-- [1225] 报告系统状态的连续日期
--

-- @lc code=start
# Write your MySQL query statement below
/*  参考 [1285] 找到连续区间的开始和结束数字 */
SELECT      period_state, 
            MIN(happen_date) AS `start_date`, 
            MAX(happen_date) AS `end_date`
FROM 
    (SELECT  fail_date AS 'happen_date', 
            DAYOFYEAR(fail_date) - RANK() OVER (ORDER BY fail_date ASC) AS `reference`, 
            'failed' AS `period_state`
    FROM    Failed 
    WHERE   fail_date LIKE '2019%'
    UNION 
    SELECT  success_date AS 'happen_date', 
            DAYOFYEAR(success_date) - RANK() OVER (ORDER BY success_date ASC) AS `reference`, 
            'succeeded' AS `period_state`
    FROM    Succeeded
    WHERE   success_date LIKE '2019%'
    ) AS `T`
GROUP BY    period_state, reference
ORDER BY    MIN(happen_date) ASC

-- @lc code=end

