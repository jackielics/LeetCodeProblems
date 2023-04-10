--
-- @lc app=leetcode.cn id=612 lang=mysql
--
-- [612] 平面上的最近距离
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  ROUND(
            SQRT(
                POW(P1.x - P2.x, 2) + 
                POW(P1.y - P2.y, 2)
            ), 
            2
        ) AS `shortest`
FROM    Point2D P1, Point2D P2
WHERE   P1.x <> P2.x 
        OR  P1.y <> P2.y
ORDER BY `shortest` ASC
LIMIT 1

/* 大神的方法：避免重复计算，用MIN避免排序 */
SELECT
    ROUND(
        SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))),
        2
    ) AS shortest
FROM    Point2D p1,
    JOIN Point2D p2 ON (
        p1.x <= p2.x
        AND p1.y <> p2.y
    )
    OR (
        p1.x < p2.x
        AND p1.y = p2.y
    )
-- @lc code=end

