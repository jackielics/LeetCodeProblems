--
-- @lc app=leetcode.cn id=1747 lang=mysql
--
-- [1747] 应该被禁止的 Leetflex 账户
--

-- @lc code=start
/* select distinct a.account_id
from LogInfo a
left join LogInfo b
on a.account_id = b.account_id
    and a.ip_address <> b.ip_address
    and ((a.login between b.login and b.logout)
        or (a.logout between b.login and b.logout)) */
# Write your MySQL query statement below
SELECT DISTINCT a.account_id
FROM LogInfo a
INNER JOIN LogInfo b
ON a.account_id = b.account_id AND a.ip_address <> b.ip_address AND ((a.login between b.login and b.logout) OR (a.logout between b.login and b.logout))
-- @lc code=end

