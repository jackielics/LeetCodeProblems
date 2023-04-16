--
-- @lc app=leetcode.cn id=1174 lang=mysql
--
-- [1174] 即时食物配送 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	ROUND(
			COUNT(
				CASE 
					WHEN order_date = customer_pref_delivery_date THEN 1
					ELSE NULL
				END
			) / COUNT(*) *100, 
			2) AS immediate_percentage
FROM 
	(SELECT 	delivery_id, 
			customer_id, 
			order_date, 
			customer_pref_delivery_date, 
			ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS customer_order_number
	FROM 	Delivery ) AS T
WHERE 	customer_order_number = 1 -- 筛选首单

/* 大神的方法：用(,) in (select...)来筛选 */
select round (
    sum(order_date = customer_pref_delivery_date) * 100 /
    count(*),
    2
) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
    select customer_id, min(order_date)
    from delivery
    group by customer_id
)
-- @lc code=end

