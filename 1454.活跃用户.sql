--
-- @lc app=leetcode.cn id=1454 lang=mysql
--
-- [1454] 活跃用户
--
-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT
    id, 
    name
FROM    
(SELECT DISTINCT --
    id,
    login_date,
    DATEDIFF(login_date, '1969-01-01') - DENSE_RANK() OVER (
        PARTITION BY id
        ORDER BY login_date ASC
    ) AS `reference`
FROM
    Logins ) AS `t`
    LEFT JOIN Accounts USING(id)
GROUP BY    id, reference
# 筛选出连续五天以上活跃的id
HAVING  COUNT(*) >= 5
ORDER BY    id ASC

/* 大神的解法:行不通！ */
/* SELECT DISTINCT
        id, 
        name
FROM 
    (SELECT  DISTINCT
            L1.id
    FROM    Logins L1
            JOIN    Logins L2
                ON  L1.id = L2.id
                AND DATEDIFF(L2.login_date, L1.login_date) 
                    BETWEEN 0 AND 4
    GROUP BY    L1.id, L1.login_date
    HAVING  COUNT(*) >= 5
    ORDER BY    L1.id ASC) AS `T`
        LEFT JOIN Accounts USING(id) */
-- @lc code=end