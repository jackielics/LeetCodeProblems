--
-- @lc app=leetcode.cn id=1831 lang=mysql
--
-- [1831] 每天的最大交易
--

-- @lc code=start
# Write your MySQL query statement below

SELECT transaction_id
FROM Transactions AS T1
    LEFT JOIN  (SELECT  @var AS 'day',
                        max(amount) AS 'max_amount'        
                FROM Transactions t
                GROUP BY @var := DATE_FORMAT(t.day, '%Y-%m-%d')) AS T2
    ON DATE_FORMAT(T1.day, '%Y-%m-%d') = T2.day
WHERE T1.amount = T2.max_amount
ORDER BY transaction_id

/* 上面是麻烦的做法，下面的窗口函数的简短做法 */
SELECT transaction_id 
FROM    (SELECT transaction_id, 
                T1.day, 
                amount, 
                MAX(amount) OVER (PARTITION BY DATE_FORMAT(T1.day, '%Y-%m-%d')) AS 'max_amount'
         FROM   Transactions T1) AS T
WHERE amount = max_amount
ORDER BY transaction_id ASC 

-- @lc code=end

