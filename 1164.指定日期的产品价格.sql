--
-- @lc app=leetcode.cn id=1164 lang=mysql
--
-- [1164] 指定日期的产品价格
--

-- @lc code=start
# Write your MySQL query statement below
WITH CTE AS
(SELECT
    product_id,
    MAX(change_date) AS change_date
FROM 
    Products
WHERE
    change_date <= "2019-08-16"
GROUP BY
    product_id)

-- 目标日期前没变过价格的
SELECT 
    product_id,
    10 AS price
FROM 
    Products
WHERE 
    product_id NOT IN (
        SELECT product_id 
        FROM CTE
        )
UNION 
SELECT
    c.product_id,
    p.new_price
FROM
    CTE c
LEFT JOIN
    Products p
ON 
    c.product_id = p.product_id
    AND c.change_date = p.change_date
-- @lc code=end

