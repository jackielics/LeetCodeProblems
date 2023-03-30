--
-- @lc app=leetcode.cn id=1890 lang=mysql
--
-- [1890] 2020年最后一次登录
--

-- @lc code=start
# Write your MySQL query statement below
/* 编写一个 SQL 查询，该查询可以获取在 2020 年登录过的所有用户的本年度 最后一次 登录时间。结果集 不 包含 2020 年没有登录过的用户。 */
/* 返回的结果集可以按 任意顺序 排列。 */
select user_id, max(time_stamp) as last_stamp
from Logins
where time_stamp like '2020%'
group by user_id
-- @lc code=end

