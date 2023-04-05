-- 
-- @lc app=leetcode.cn id=1613 lang=mysql 
-- 
-- [1613] 找到遗失的ID 
-- 
-- @lc code=start 
# Write your MySQL query statement below 
WITH RECURSIVE hundred(num) AS ( 
    SELECT (1)
    UNION ALL
    SELECT num+1 
    FROM hundred 
    WHERE num<( SELECT MAX(customer_id)
                FROM Customers 
                )
)
SELECT num AS 'ids'
FROM hundred
WHERE num NOT IN (SELECT customer_id 
                    FROM Customers )
ORDER BY ids
-- @lc code=end 