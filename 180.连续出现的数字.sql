--
-- @lc app=leetcode.cn id=180 lang=mysql
--
-- [180] 连续出现的数字
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
    DISTINCT num AS ConsecutiveNums
FROM
    (SELECT
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS num1,
        LAG(num, 1) OVER (ORDER BY id) AS num2
    FROM
        Logs) t
WHERE
    num = num1 
    AND num = num2
-- @lc code=end

