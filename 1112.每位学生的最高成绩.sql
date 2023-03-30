--
-- @lc app=leetcode.cn id=1112 lang=mysql
--
-- [1112] 每位学生的最高成绩
--

-- @lc code=start
# Write your MySQL query statement below
select  student_id, 
    (select min(e2.course_id) 
        from Enrollments e2 
        where e2.grade = max(e1.grade)
            and e2.student_id = e1.student_id
        ) as course_id, 
    max(e1.grade) as grade
from Enrollments e1
group by student_id
order by student_id asc
-- @lc code=end

