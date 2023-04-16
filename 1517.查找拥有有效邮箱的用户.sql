--
-- @lc app=leetcode.cn id=1517 lang=mysql
--
-- [1517] 查找拥有有效邮箱的用户
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 	user_id, 
		name, 
		mail
FROM 	Users
WHERE 	mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
/* --对于字符转义，MySQL中的正则表达式需要额外添加一个反斜杠\，所以需要两个反斜杠\\ */
/* 或者 '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$' */
-- @lc code=end

