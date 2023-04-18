--
-- @lc app=leetcode.cn id=1322 lang=mysql
--
-- [1322] 广告效果
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	ad_id, 
		IFNULL(ROUND(
			SUM(IF(action = 'Clicked', 1, 0)) 
			/ 
			SUM(IF(action IN ('Clicked', 'Viewed') , 1, 0))
			* 100, 2), 0.00) AS ctr
FROM 	Ads
GROUP BY	ad_id
ORDER BY	ctr DESC, ad_id ASC

/* 大神的解法：用SUM(条件)直接计数，6，更加精简*/
SELECT ad_id,
    ROUND(IFNULL(SUM(action = 'Clicked') /
        (SUM(action = 'Clicked') + SUM(action = 'Viewed')) * 100, 0), 2) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id ASC;
-- @lc code=end

