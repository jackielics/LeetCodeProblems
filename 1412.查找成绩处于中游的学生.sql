--
-- @lc app=leetcode.cn id=1412 lang=mysql
--
-- [1412] 查找成绩处于中游的学生
--

-- @lc code=start
# Write your MySQL query statement below

/* 每个测验的最高最低分 */
WITH M_Exam AS
(SELECT e1.exam_id, 
        e1.student_id, 
        e1.score, 
        e2.min_score, 
        e2.max_score
FROM    Exam e1
        LEFT JOIN   (
            SELECT  e.exam_id, 
                    MIN(e.score) AS 'min_score',
                    MAX(e.score) AS 'max_score'
            FROM    Exam e
            GROUP BY    e.exam_id
        ) AS e2
        ON  e1.exam_id = e2.exam_id)

SELECT  DISTINCT M_Exam.student_id, 
        Student.student_name
FROM    M_Exam
        LEFT JOIN   Student
        ON  M_Exam.student_id = Student.student_id
WHERE   Student.student_id NOT IN
        (SELECT  m.student_id
        FROM    M_Exam m
        WHERE   m.score = m.min_score
                OR  m.score = m.max_score)
ORDER BY    Student.student_id
-- @lc code=end

