--
-- @lc app=leetcode.cn id=1635 lang=mysql
--
-- [1635] Hopper 公司查询 I
--

-- @lc code=start
# Write your MySQL query statement below
/* WITH RECURSIVE month_table(`month`) AS
(
        SELECT 1
        UNION 
        SELECT `month`+1 
        FROM month_table 
        WHERE `month` < 12
), month_drivers AS
(SELECT  m.`month`,
        IFNULL(active_drivers,0) AS active_drivers
FROM    month_table m
        LEFT JOIN
                (SELECT  DATE_FORMAT(join_date, '%Y') AS `year`, 
                        DATE_FORMAT(join_date, '%m') AS `month`, 
                        COUNT(*) OVER (ORDER BY DATE_FORMAT(join_date, '%Y-%m') ASC) AS active_drivers 
                FROM    Drivers
                ORDER BY     DATE_FORMAT(join_date, '%Y-%m')) AS `D`
        ON      D.`year` = 2020
                AND     m.`month` = D.`month`)


SELECT  DISTINCT * -- 这里会出现重复值，暂时不知道原因
FROM    
        (SELECT  `month`, 
                (       SELECT  MAX(m2.active_drivers)
                        FROM    month_drivers m2
                        WHERE   m2.`month` <= m1.`month`
                        ) AS active_drivers -- 避免出现空值
        FROM    month_drivers m1) AS `T2`
        LEFT JOIN 
                (SELECT  `month`, 
                        IFNULL(accepted_rides, 0) AS accepted_rides
                FROM    month_table
                        LEFT JOIN
                                (SELECT  MONTH(requested_at) AS `month`, 
                                        COUNT(*) AS `accepted_rides`
                                FROM    AcceptedRides
                                        LEFT JOIN   Rides
                                        USING(ride_id)
                                WHERE   YEAR(requested_at) = 2020
                                GROUP BY        MONTH(requested_at)) AS `T`
                        USING(`month`)) AS `T1`
        USING(`MONTH`) */

/* 大神的解法 ：区别主要在于LEFT JOIN时将
ON 202000 + month >= DATE_FORMAT没有一对一拼接，便于计算前置数量*/

WITH RECURSIVE A AS (
        SELECT
                1 month
        UNION
        ALL
        SELECT
                month + 1
        FROM
                A
        WHERE
                month <= 11
)
SELECT
        B.month,
        B.active_drivers,
        IFNULL(C.accepted_rides, 0) AS accepted_rides
FROM
        (
                SELECT
                        month,
                        IFNULL (COUNT(driver_id), 0) active_drivers
                FROM
                        A
                        LEFT JOIN Drivers 
                        ON 202000 + month >= DATE_FORMAT(join_date,'%Y%m')
                GROUP BY
                        month
        ) B
        LEFT JOIN (
                        SELECT
                                MONTH(requested_at) AS `month`,
                                COUNT(*) accepted_rides
                        FROM
                                Rides
                                JOIN AcceptedRides 
                                USING(ride_id)
                        WHERE
                                YEAR(requested_at) = 2020
                        GROUP BY MONTH(requested_at)
                ) C 
        USING (month)
ORDER BY
        month
-- @lc code=end

