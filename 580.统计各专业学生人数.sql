--
-- @lc app=leetcode.cn id=580 lang=mysql
--
-- [580] 统计各专业学生人数
--

-- @lc code=start
# Write your MySQL query statement below
select d.dept_name as dept_name, ifnull(sn.student_number, 0) as student_number
from (
    select s.dept_id as dept_id, count(*) as student_number
    from Student s
    group by s.dept_id
) as sn
right join Department d
on  d.dept_id = sn.dept_id
order by student_number desc, dept_name asc

/* select s.dept_id as dept_id # , count(*) as student_number
    from Student s
    group by s.dept_id */
-- @lc code=end

