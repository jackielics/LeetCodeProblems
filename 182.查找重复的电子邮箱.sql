--
-- @lc app=leetcode.cn id=182 lang=mysql
--
-- [182] 查找重复的电子邮箱
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
    email Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(id) > 1
-- @lc code=end

