--
-- @lc app=leetcode.cn id=1907 lang=mysql
--
-- [1907] 按分类统计薪水
--

-- @lc code=start
# Write your MySQL query statement below

SELECT 	"Low Salary" AS category, 
		COUNT(account_id) AS accounts_count
FROM 	Accounts 
WHERE 	income < 20000
UNION ALL
SELECT 	"Average Salary" AS category, 
		COUNT(account_id) AS accounts_count
FROM 	Accounts 
WHERE 	income BETWEEN 20000 AND 50000
UNION ALL
SELECT 	"High Salary" AS category, 
		COUNT(account_id) AS accounts_count
FROM 	Accounts
WHERE 	income > 50000

-- @lc code=end

