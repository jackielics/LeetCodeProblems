--
-- @lc app=leetcode.cn id=1098 lang=mysql
--
-- [1098] 小众书籍
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	book_id, 
		name
FROM	Books
		LEFT JOIN (
			(SELECT	book_id, 
					SUM(quantity) AS total_quantity
			FROM	Orders
			WHERE	DATEDIFF('2019-06-23', dispatch_date) <=365
			GROUP BY	book_id)
		) AS T
		USING(book_id)
WHERE	DATEDIFF('2019-06-23', available_from) >=30
		AND (total_quantity IS NULL
		OR total_quantity < 10)

/* 大神的解法：在on后面添加条件对LEFT JOIN的表进行限制，用ifnull同时进行判空和判值 */
select b.book_id, name
from books b left join orders o
on b.book_id = o.book_id and dispatch_date >= '2018-06-23'
where available_from < '2019-05-23'
group by b.book_id
having ifnull(sum(quantity), 0) < 10
-- @lc code=end

