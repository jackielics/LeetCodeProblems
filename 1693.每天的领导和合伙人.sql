--
-- @lc app=leetcode.cn id=1693 lang=mysql
--
-- [1693] 每天的领导和合伙人
--

-- @lc code=start
# Write your MySQL query statement below
/* 写一条 SQL 语句，使得对于每一个 date_id 和 make_name，返回不同的 lead_id 以及不同的 partner_id 的数量。
按 任意顺序 返回结果表。 */
select date_id,make_name,count(distinct(lead_id)) as unique_leads,count(distinct(partner_id)) as unique_partners
from DailySales
group by date_id,make_name
-- @lc code=end

