--
-- @lc app=leetcode.cn id=1532 lang=mysql
--
-- [1532] 最近的三笔订单
--
-- @lc code=start
# Write your MySQL query statement below
/* with order_cnt as (
 select 
 from Orders
 group by order_id
 having count(*) >= 3
 )
 select
 customer_name,
 customer_id,
 order_id,
 order_date  */
SELECT name as 'customer_name', customer_id, order_id, order_date
FROM 
    (SELECT
        name, 
        Orders.customer_id,
        order_id,
        order_date,
        RANK() OVER (
            PARTITION BY customer_id
            ORDER BY
                order_date DESC
        ) as 'rk'
    FROM
        Orders
        LEFT JOIN Customers 
        ON Orders.customer_id = Customers.customer_id
    ORDER BY
        name ASC, Orders.customer_id ASC, order_date DESC) AS Orders_Customers
WHERE rk <= 3
    -- @lc code=end