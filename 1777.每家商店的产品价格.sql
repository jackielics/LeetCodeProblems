--
-- @lc app=leetcode.cn id=1777 lang=mysql
--
-- [1777] 每家商店的产品价格
--

-- @lc code=start
# Write your MySQL query statement below
/* 行转换列 */
SELECT product_id,
       SUM(CASE store WHEN 'store1' THEN price ELSE NULL END) AS 'store1',
       SUM(CASE store WHEN 'store2' THEN price ELSE NULL END) AS 'store2',
       SUM(CASE store WHEN 'store3' THEN price ELSE NULL END) AS 'store3'
FROM products
GROUP BY product_id

-- @lc code=end

