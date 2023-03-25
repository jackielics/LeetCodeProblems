# Write your MySQL query statement below
# 写出一个SQL 查询语句，计算每个雇员的奖金。如果一个雇员的id是奇数并且他的名字不是以'M'开头，那么他的奖金是他工资的100%，否则奖金为0。

# Return the result table ordered by employee_id.

# 返回的结果集请按照employee_id排序。
SELECT  employee_id, IF(employee_id % 2 = 1 AND name NOT LIKE 'M%', salary, 0) AS bonus
FROM Employee
ORDER BY employee_id