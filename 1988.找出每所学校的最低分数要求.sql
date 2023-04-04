--
-- @lc app=leetcode.cn id=1988 lang=mysql
--
-- [1988] 找出每所学校的最低分数要求
--

-- @lc code=start
# Write your MySQL query statement below
/* SELECT score, student_count, RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Exam */

select
    school_id,
    ifnull(min(score), -1) as score
from
(
    select
        s.school_id,
        e.score
    from schools s
    left join exam e on
        s.capacity >= e.student_count
) tmp
group by school_id

-- @lc code=end

/* select (select count(e2.score)
        from Exam e2
        where e2.score >= e1.score
    ) as 'rank', 
    (   select ifnull(sum(e3.student_count), 0) as total_count
        from Exam e3
        where e3.score >= e1.score
    )as 'total_count' */
/* from Exam e1 */

/* select ifnull(sum(e2.student_count), 0) as total_count
from Exam e2
where e2.score >= 966 */

/* select count(*)
        from Exam e2
        where e2.score >= 975 */