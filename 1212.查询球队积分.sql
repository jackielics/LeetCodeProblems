--
-- @lc app=leetcode.cn id=1212 lang=mysql
--
-- [1212] 查询球队积分
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	team_id, 
		team_name, 
		SUM(
			# 赢3平1输0 
			CASE 
				WHEN	team_id = host_team -- as host
						THEN	(CASE
										WHEN host_goals > guest_goals THEN 3
										WHEN host_goals = guest_goals THEN 1
										ELSE 0
									END)
				WHEN	team_id = guest_team -- as host
						THEN  	(CASE	-- as guest
									WHEN host_goals > guest_goals THEN 0
									WHEN host_goals = guest_goals THEN 1
									ELSE 3
								END)
				ELSE	0
			END
		) AS num_points
FROM 	(
		SELECT 	*
		FROM 	Teams
		LEFT JOIN	Matches
		ON 	team_id = host_team
		UNION ALL
		SELECT 	*
		FROM 	Teams
		LEFT JOIN	Matches M
		ON 	team_id = guest_team
		) AS T
GROUP BY	T.team_id
ORDER BY	num_points DESC, team_id ASC

/* 大神的解法：直接join不进行union，可能比较费空间 */
select team_id,team_name,sum(case when team_id = host_team and host_goals > guest_goals then 3 
                            when team_id = host_team and host_goals = guest_goals then 1 else 0  end)+
                            sum(case when team_id = guest_team and guest_goals > host_goals then 3 
                            when team_id = guest_team and guest_goals = host_goals then 1 else 0  end) as num_points
from Teams join Matches
group by team_id
order by num_points desc,team_id
-- @lc code=end

