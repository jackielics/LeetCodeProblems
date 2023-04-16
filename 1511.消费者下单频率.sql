--
-- @lc app=leetcode.cn id=1511 lang=mysql
--
-- [1511] 消费者下单频率
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	customer_id, 
		name
FROM
	(SELECT	customer_id, 
			name, 
			SUM(IF(order_date REGEXP '^2020-06.*', quantity * price, 0)
				) AS amount_06,
			SUM(IF(order_date REGEXP '^2020-07.*', quantity * price, 0)
				) AS amount_07
	FROM 	Orders 
			LEFT JOIN	Product 
			USING(product_id)
			LEFT JOIN 	Customers
			USING(customer_id)
	GROUP BY	customer_id ) AS T
WHERE 	amount_06 >= 100 
		AND amount_07 >= 100

/* 大神的解法：用GROUP BY里的having替代临时表 */
select c.customer_id,c.name
from customers c
join orders o on o.customer_id=c.customer_id
join product p on p.product_id=o.product_id
group by c.customer_id, c.name
having sum(case when left(o.order_date,7)='2020-06' then p.price*o.quantity else 0 end)>=100 and
sum(case when left(o.order_date,7)='2020-07' then p.price*o.quantity else 0 end)>=100
-- @lc code=end

