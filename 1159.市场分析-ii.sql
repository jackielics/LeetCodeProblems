--
-- @lc app=leetcode.cn id=1159 lang=mysql
--
-- [1159] 市场分析 II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	user_id AS seller_id, 
		IF(item_brand IS NULL, 'no', 'yes') AS 2nd_item_fav_brand
FROM	Users
		LEFT JOIN
			(SELECT	seller_id, 
					item_brand
			FROM 	
				(SELECT	*, 
						RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS rk
				FROM	Orders
						LEFT JOIN	Users 
						ON 			Orders.seller_id = Users.user_id
						LEFT JOIN	Items
						USING(item_id)) AS T
			WHERE	rk = 2
					AND	item_brand = favorite_brand) AS T2
		ON 		Users.user_id = T2.seller_id
-- @lc code=end

