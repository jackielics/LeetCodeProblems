--
-- @lc app=leetcode.cn id=2010 lang=mysql
--
-- [2010] 职员招聘人数 II
--

-- @lc code=start
# Write your MySQL query statement below
/* WITH SeniorCandidates AS
(SELECT  employee_id, 
        experience, 
        salary, 
        70000 - SUM(salary) OVER(ORDER BY salary ASC) AS `remaining`
FROM    Candidates 
WHERE   experience = 'Senior'),
JuniorCandidates AS
(SELECT  employee_id, 
        experience, 
        salary, 
        IFNULL(( -- 一个Senior都请不起
            SELECT  MIN(SC.remaining)
            FROM    SeniorCandidates SC
            WHERE   SC.remaining > 0
        ), 70000) - SUM(salary) OVER(ORDER BY salary ASC) AS `remaining`
FROM    Candidates
WHERE   experience = 'Junior')

SELECT  employee_id
FROM    SeniorCandidates
WHERE   remaining >= 0
UNION
SELECT  employee_id 
FROM    JuniorCandidates
WHERE   remaining >= 0 */

/* 大神的代码：先过滤Senior，再过滤Junior */
select 
    employee_id
from
    (
        select
            *,
            70000 - sum(salary) over(
                order by
                    experience_rk,
                    salary
            ) as sum_salary2
        from
            (
                select
                    *,
                    70000 - sum(salary) over(
                        partition by experience
                        order by
                            salary
                    ) as sum_salary,
                    -- 方便排序时将Senior排在前面
                    if(experience = 'Senior', 1, 2) as experience_rk
                from
                    candidates
            ) t
        where
            t.sum_salary >= 0 -- 筛选掉雇不了的Senior
    ) t2 -- t2中的Senior都是可以雇佣的
where
    t2.sum_salary2 >= 0 -- 进一步筛选掉雇不了的Junior
-- @lc code=end

