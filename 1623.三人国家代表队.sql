--
-- @lc app=leetcode.cn id=1623 lang=mysql
--
-- [1623] 三人国家代表队
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	A.student_name AS member_A, 
		B.student_name AS member_B, 
		C.student_name AS member_C
FROM	SchoolA AS A, 
		SchoolB AS B, 
		SchoolC AS C
WHERE	A.student_id != B.student_id
		AND A.student_id != C.student_id
		AND B.student_id != C.student_id
		AND A.student_name != B.student_name
		AND B.student_name != C.student_name
		AND A.student_name != C.student_name

/* 大神的解法：同时连接两表*/
SELECT a.student_name AS member_A, b.student_name AS member_B, c.student_name AS member_C
FROM SchoolA a 
JOIN (SchoolB b,SchoolC c)
ON (
    a.student_name <> b.student_name 
    AND a.student_id <> b.student_id
    AND a.student_name <> c.student_name 
    AND a.student_id <> c.student_id 
    AND b.student_name <> c.student_name 
    AND b.student_id <> c.student_id
)
-- @lc code=end

