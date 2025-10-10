--
-- @lc app=leetcode.cn id=175 lang=mysql
--
-- [175] 组合两个表
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
    FirstName firstName,
    LastName lastName,
    City city,
    State state
FROM
    Person p
LEFT JOIN 
    Address a
ON 
    p.PersonId = a.PersonId
-- @lc code=end

