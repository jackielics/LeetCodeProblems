--
-- @lc app=leetcode.cn id=1280 lang=mysql
--
-- [1280] 学生们参加各科测试的次数
--

-- @lc code=start
# Write your MySQL query statement below
select st.student_id, 
    st.student_name, 
    su.subject_name, 
    (
        select count(*)
        from Examinations ex
        where ex.student_id = st.student_id
            and ex.subject_name  = su.subject_name
    ) as attended_exams 
from Students st, Subjects su
order by st.student_id, su.subject_name
-- @lc code=end

