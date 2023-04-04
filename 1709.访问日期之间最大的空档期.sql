--
-- @lc app=leetcode.cn id=1709 lang=mysql
--
-- [1709] 访问日期之间最大的空档期
--

-- @lc code=start
# Write your MySQL query statement below

/* 对于每个user_id，找出刚好比当前visit_date大的日期*/
# 在大于当前的日期中找出最小的

/* with uv as
(select  user_id, 
            visit_date,
            ifnull(
                (select min(uv2.visit_date)
                from UserVisits uv2
                where   uv2.user_id = uv1.user_id
                and uv2.visit_date > uv1.visit_date)
            , '2021-1-1') as 'next_date'
        from UserVisits uv1)

select  user_id, 
        max(datediff(next_date, visit_date)) as 'biggest_window'
from    uv 
group by    user_id  */

/* 大神的解法 */

/* SELECT
    user_id,
    visit_date,
    LEAD(visit_date, 1, '2021-1-1') OVER (PARTITION BY user_id ORDER BY visit_date) AS next_day # 根据user_id分批，按照时间正序取lead
FROM UserVisits */

/* SELECT
    user_id,
    MAX(DATEDIFF(next_day, visit_date)) AS biggest_window
FROM (
    SELECT
        user_id,
        visit_date,
        LEAD(visit_date, 1, '2021-1-1') OVER (PARTITION BY user_id ORDER BY visit_date) AS next_day
    FROM UserVisits
) tmp
GROUP BY user_id
ORDER BY user_id */

select user_id, DENSE_RANK() over (order by user_id asc) as 'rk'
from UserVisits uv


-- @lc code=end

