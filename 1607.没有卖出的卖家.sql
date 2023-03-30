--

-- @lc app=leetcode.cn id=1607 lang=mysql

--

-- [1607] 没有卖出的卖家

--

-- @lc code=start

# Write your MySQL query statement below
select seller_name
from Seller
where seller_id not in (
        select seller_id
        from Orders
        where sale_date like '2020%'
    ) 
order by seller_name asc
-- @lc code=end