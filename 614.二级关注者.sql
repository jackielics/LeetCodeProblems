--
-- @lc app=leetcode.cn id=614 lang=mysql
--
-- [614] 二级关注者
--

-- @lc code=start
# Write your MySQL query statement below

SELECT  followee AS `follower`, 
        COUNT(*) AS `num`
FROM    follow F1
WHERE   followee IN ( -- 只对关注者进行统计
            SELECT  F2.follower
            FROM    follow F2
        )
GROUP BY    followee
ORDER BY    `follower` ASC
-- @lc code=end

