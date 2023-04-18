--
-- @lc app=leetcode.cn id=1194 lang=mysql
--
-- [1194] 锦标赛优胜者
--

-- @lc code=start
# Write your MySQL query statement below
SELECT	group_id, 
		player_id
FROM	
	(SELECT	player_id, 
			SUM(sum_score) AS sum_score, 
			RANK() OVER(PARTITION BY group_id ORDER BY SUM(sum_score) DESC, player_id ASC) AS rk
	FROM	
		(SELECT	first_player AS player_id, 
				SUM(first_score) AS sum_score
		FROM	Matches
		GROUP BY	first_player
		UNION ALL
		SELECT	second_player AS player_id, 
				SUM(second_score) AS sum_score
		FROM	Matches
		GROUP BY	second_player
		) AS T
		LEFT JOIN	Players 
		USING(player_id)
	GROUP BY	player_id) AS T1
	LEFT JOIN	Players
	USING(player_id)
WHERE	rk = 1

/* 大神的方法：用GROUP BY 输出第一条代替排序*/
SELECT group_id, player_id
FROM (
    SELECT group_id, player_id, SUM(score) AS score
    FROM (
        -- 每个用户总的 first_score
        SELECT Players.group_id, Players.player_id, SUM(Matches.first_score) AS score
        FROM Players JOIN Matches ON Players.player_id = Matches.first_player
        GROUP BY Players.player_id

        UNION ALL

        -- 每个用户总的 second_score
        SELECT Players.group_id, Players.player_id, SUM(Matches.second_score) AS score
        FROM Players JOIN Matches ON Players.player_id = Matches.second_player
        GROUP BY Players.player_id
    ) s
    GROUP BY player_id
    ORDER BY score DESC, player_id
) result
GROUP BY group_id

-- @lc code=end

