--
-- @lc app=leetcode.cn id=1384 lang=mysql
--
-- [1384] 按年度列出销售总额
--

-- @lc code=start
# Write your MySQL query statement below
/* WITH YearsSales AS
(SELECT product_id, 
        average_daily_sales, 
        (
            CASE
                -- 18年开始18年结束
                WHEN    period_start LIKE '2018%'
                        THEN (
                            CASE
                                WHEN    period_end LIKE '2018%' 
                                        THEN DATEDIFF(period_end, period_start) + 1
                                WHEN    period_end LIKE '2019%'
                                        OR period_end LIKE '2020%' 
                                        THEN DATEDIFF('2018-12-31', period_start) + 1
                                WHEN period_end LIKE '2020%' THEN DATEDIFF('2018-12-31', period_start) + 1
                            END
                        )
                ELSE    0
            END
        ) AS 'days_of_2018', 

        (
            CASE
                WHEN    period_start LIKE '2018%' 
                        THEN (
                            CASE
                                WHEN    period_end LIKE '2018%' 
                                        THEN 0
                                WHEN    period_end LIKE '2019%' 
                                        THEN DATEDIFF(period_end, '2019-01-01') + 1
                                WHEN    period_end LIKE '2020%' 
                                        THEN 365
                            END
                        )
                WHEN    period_start LIKE '2019%' 
                        THEN (
                            CASE
                                WHEN    period_end LIKE '2019%' 
                                        THEN DATEDIFF(period_end, period_start) + 1
                                WHEN    period_end LIKE '2020%' 
                                        THEN DATEDIFF('2019-12-31', period_start) + 1
                            END
                        )
                ELSE    0
            END
        ) AS 'days_of_2019', 

        (
            CASE
                WHEN    period_end  LIKE '2020%' 
                        THEN (
                            CASE    
                                WHEN    period_start LIKE '2020%' 
                                        THEN DATEDIFF(period_end, period_start) + 1
                                WHEN    period_start LIKE '2019%' 
                                        OR period_start LIKE '2018%'
                                        THEN DATEDIFF(period_end, '2020-01-01') + 1
                            END 
                        )
                ELSE    0
            END
        ) AS 'days_of_2020'
FROM    Sales)

SELECT  product_id, 
        product_name, 
        '2018' AS report_year,
        (average_daily_sales * days_of_2018) AS total_amount
FROM    YearsSales y
        LEFT JOIN Product p
        USING(product_id)
WHERE   days_of_2018 > 0
UNION ALL
SELECT  product_id, 
        product_name, 
        '2019' AS report_year,
        (average_daily_sales * days_of_2019) AS total_amount
FROM    YearsSales y
        LEFT JOIN Product p
        USING(product_id)
WHERE   days_of_2019 > 0
UNION ALL
SELECT  product_id, 
        product_name, 
        '2020' AS report_year,
        (average_daily_sales * days_of_2020) AS total_amount
FROM    YearsSales y
        LEFT JOIN Product p
        USING(product_id)
WHERE   days_of_2020 > 0
ORDER BY product_id, report_year */

/* 大神的解法 */
select
    s.product_id,
    p.product_name,
    y.year report_year,
    s.average_daily_sales * (
        if(
            year(s.period_end) > y.year,    -- 不在此年结束
            y.days_of_year,                 -- 则一整年
            dayofyear(s.period_end)         -- 结束那年销售的天数
        ) - if(                             -- 日期可以直接减
            year(s.period_start) < y.year,  -- 不在此年开始
            1,                              -- 补偿减去的天数
            dayofyear(s.period_start)       -- 开始那年没有销售的天数
        ) + 1
    ) total_amount
from
    Sales s
    -- 将订单以年份来划分
    inner join (
        select
            '2018' year,
            365 days_of_year
        union
        all
        select
            '2019' year,
            365 days_of_year
        union
        all
        select
            '2020' year,
            366 days_of_year
    ) y on y.year between year(s.period_start) and year(s.period_end)
    inner join Product p on p.product_id = s.product_id
order by
    s.product_id,
    y.year

/* SELECT  *
FROM    Sales s
inner join (
        select
            '2018' year,
            365 days_of_year
        union
        all
        select
            '2019' year,
            365 days_of_year
        union
        all
        select
            '2020' year,
            366 days_of_year
    ) y on y.year between year(s.period_start) and year(s.period_end) */


-- @lc code=end

