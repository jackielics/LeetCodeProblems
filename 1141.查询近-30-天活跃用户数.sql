--
-- @lc app=leetcode.cn id=1141 lang=mysql
--
-- [1141] 查询近30天活跃用户数
--

-- @lc code=start
# Write your MySQL query statement below
select activity_date as day,count(distinct user_id) as active_users
from Activity
where activity_date between SUBDATE('2019-07-27',INTERVAL 29 day) and '2019-07-27'
group by activity_date
-- @lc code=end
/* 请写SQL查询出截至 2019-07-27（包含2019-07-27），近 30 天的每日活跃用户数（当天只要有一条活动记录，即为活跃用户）。
以 任意顺序 返回结果表。 */


