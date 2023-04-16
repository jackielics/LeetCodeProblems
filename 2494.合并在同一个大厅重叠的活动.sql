--
-- @lc app=leetcode.cn id=2494 lang=mysql
--
-- [2494] 合并在同一个大厅重叠的活动
--

-- @lc code=start
# Write your MySQL query statement below

# Write your MySQL query statement below

-- 有点疑惑，要是有不止两个重叠的情况怎么办？
-- 需要合并的情况：怎么算重叠/冲突？如何判断？
/* 排除法：不重叠的情况：start_day1 > end_day2 或者 start_day2 > end_day1 
相当于start_day1 > start_day2 and start_day1 < end_day2，
或者start_day2 > start_day1 and start_day2 < end_day1 */

WITH Hall AS
(
        SELECT  H1.hall_id AS `hall_id`, 
        H1.start_day AS `H1_start_day`, 
        H1.end_day AS `H1_end_day`, 
        H2.start_day AS `H2_start_day`, 
        H2.end_day AS `H2_end_day`, 
        LEAST(H1.start_day, H2.start_day) AS `period_start_day`, 
        GREATEST(H1.end_day, H2.end_day) AS `period_end_day` 
        FROM    HallEvents H1
        LEFT JOIN HallEvents H2
        -- 要避免拼接自身
        ON   H1.hall_id = H2.hall_id -- 两两合并
                AND (H1.start_day <> H2.start_day OR H1.end_day <> H2.end_day) -- 避免重复
        -- H1的start_day在H2的start_day和end_day之间
                AND (H2.start_day BETWEEN H1.start_day AND H1.end_day)
), Hall_not_null AS
(
        SELECT  hall_id, 
                period_start_day    AS `start_day`, 
                period_end_day      AS `end_day`
        FROM    Hall
        WHERE   H2_start_day IS NOT NULL
)


SELECT  hall_id, 
        start_day, 
        end_day
FROM    Hall_not_null
UNION 
SELECT  hall_id, 
        start_day, 
        end_day
FROM    HallEvents H1
WHERE   NOT EXISTS(
    SELECT  *
    FROM    Hall_not_null H2
    WHERE   H1.hall_id = H2.hall_id
            AND(
                (H1.start_day BETWEEN H2.start_day AND H2.end_day)
                OR (H1.end_day BETWEEN H2.start_day AND H2.end_day)
            )
)
ORDER BY    hall_id, start_day
/* 现在的问题是只能两两合并，再多就不行了 */


/* 大神的方法：太高级了导致没看懂 */
/* with t as (
    select
        *,
        @g:=if(@h = hall_id and @e >= start_day, @g, @g + 1) as g,
        @e:=if(@h = hall_id and @e >= end_day, @e, end_day),
        @h:=hall_id
    from
        (select * from HallEvents order by hall_id, start_day) as hall,
        (select @g:=0, @e:=null, @h:=null) as init
)

select hall_id, min(start_day) as start_day, max(end_day) as end_day from t group by g */

-- @lc code=end

