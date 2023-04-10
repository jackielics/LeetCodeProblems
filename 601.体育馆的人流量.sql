--
-- @lc app=leetcode.cn id=601 lang=mysql
--
-- [601] 体育馆的人流量
--

-- @lc code=start
# Write your MySQL query statement below

SELECT  id, 
        visit_date, 
        people
FROM    
    (SELECT  *,
            COUNT(1) OVER (PARTITION BY `diff`) AS `cnt_diff`
    FROM
        (SELECT  *,
                id - `rn` AS `diff`
        FROM    
            (SELECT *, 
                    ROW_NUMBER() OVER(ORDER BY id ASC) AS `rn`
            FROM    Stadium 
            WHERE   people >= 100) AS `T`) AS `T1`) AS `T2`
WHERE   `cnt_diff` >= 3 -- 要求连续的天数
ORDER BY    visit_date ASC -- 按照日期升序排列

-- @lc code=end

