--
-- @lc app=leetcode.cn id=1369 lang=mysql
--
-- [1369] 获取最近第二次的活动
--

-- @lc code=start
# Write your MySQL query statement below
/* WITH UserActivity_RK AS
(   SELECT  username, 
            activity, 
            startDate, 
            endDate,
            RANK() OVER (   PARTITION BY username
                                ORDER BY startDate DESC) AS 'rk'
    FROM    UserActivity )

SELECT  username, 
        activity, 
        startDate, 
        endDate
FROM    UserActivity_RK
WHERE   rk = 2
UNION
SELECT  username, 
        activity, 
        startDate, 
        endDate
FROM    UserActivity_RK
GROUP BY    username
HAVING   COUNT(*) = 1 */

/* 大神的方法：通过窗口函数COUNT()计算分组内的行数 */
select username, activity, startDate, endDate
    from (select *,
                 COUNT(1) over(partition by username) cn,
                 row_number() over(partition by username order by startdate desc) rn
            from UserActivity) A
where cn = '1'
      or rn = '2'
-- @lc code=end

