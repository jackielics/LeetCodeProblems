--
-- @lc app=leetcode.cn id=1285 lang=mysql
--
-- [1285] 找到连续区间的开始和结束数字
--

-- @lc code=start
# Write your MySQL query statement below
/* 有下一个没上一个的是开始id，有上一个没下一个点的是结束id */

/* 不存在前驱则为起点，不存在后继则为终点 */

/* select  tmp.log_id  as  start_id
from (  select log_id,
        if(not exists(select * from Logs l2 where l2.log_id = l1.log_id - 1), 1, 0) as is_start,
        if(not exists(select * from Logs l2 where l2.log_id = l1.log_id + 1), 1, 0) as is_end
        from Logs l1
    ) as tmp
where tmp.is_start = 1 */

/* select ts.start_id, te.end_id
from (
    select  tmp.log_id as start_id,
        RANK() OVER (ORDER BY tmp.log_id) as 'rk'
    from (  select log_id,
            if(not exists(select * from Logs l2 where l2.log_id = l1.log_id - 1), 1, 0) as is_start,
            if(not exists(select * from Logs l2 where l2.log_id = l1.log_id + 1), 1, 0) as is_end
            from Logs l1
        ) as tmp
    where tmp.is_start = 1
) ts
left join (
        select  tmp.log_id as end_id,
        RANK() OVER (ORDER BY tmp.log_id) as 'rk'
        from (  select log_id,
                if(not exists(select * from Logs l2 where l2.log_id = l1.log_id - 1), 1, 0) as is_start,
                if(not exists(select * from Logs l2 where l2.log_id = l1.log_id + 1), 1, 0) as is_end
                from Logs l1
            ) as tmp
        where tmp.is_end = 1
) te 
on ts.rk = te.rk */

/* 题解 */
SELECT
    MIN(log_id) START_ID,
    MAX(log_id) END_ID
FROM
    (
    SELECT DISTINCT 
        log_id, 
        log_id - RANK() OVER ( ORDER BY log_id ASC ) reference
    FROM 
        Logs
    ) T
GROUP BY
    reference
ORDER BY
    START_ID

-- @lc code=end

