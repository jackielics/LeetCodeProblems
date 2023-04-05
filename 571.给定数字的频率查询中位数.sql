--
-- @lc app=leetcode.cn id=571 lang=mysql
--
-- [571] 给定数字的频率查询中位数
--

-- @lc code=start
# Write your MySQL query statement below
WITH AccuNumbers AS
(SELECT  num, 
        frequency, 
        # 用窗口函数计算所有num值小于当前num值的frequency之和
        SUM(frequency) OVER(ORDER BY num) AS `accu`, 
        SUM(frequency) OVER() AS `total`
FROM    Numbers )

/* 方法一 */
SELECT  ROUND(  IF(
                    (SELECT  SUM(frequency)
                    FROM    Numbers) % 2 = 0, 
                    (SELECT  AVG(num) 
                    FROM    AccuNumbers 
                    WHERE   accu IN (total / 2, total / 2 + 1)), 
                    (SELECT  num 
                    FROM    AccuNumbers 
                    WHERE   accu = (total + 1) / 2)
                ),
        1) AS `median`

/* 方法二 */
SELECT  ROUND(
            (
                SELECT  AVG(num)
                FROM    AccuNumbers a1
                WHERE   accu IN (
                            (SELECT  MIN(a2.accu)
                            FROM    AccuNumbers a2
                            WHERE   a2.accu >= FLOOR(a1.total / 2 + 0.5)), 
                            (SELECT  MIN(a2.accu)
                            FROM    AccuNumbers a2
                            WHERE   a2.accu >= CEIL(a1.total / 2 + 0.5))
                            )
                )
        ,1) AS `median`


-- @lc code=end

