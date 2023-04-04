--
-- @lc app=leetcode.cn id=550 lang=mysql
--
-- [550] 游戏玩法分析 IV
--

-- @lc code=start
# Write your MySQL query statement below

select round((select count(*)
                from (select distinct a1.player_id
                        from Activity a1
                        where not exists(
                                select *
                                from Activity a3
                                where a3.player_id = a1.player_id
                                and a3.event_date < a1.event_date
                        )
                        and exists(
                        select *
                        from Activity a2
                        where a2.player_id = a1.player_id
                        and a2.event_date = adddate(a1.event_date, 1)
                        )
                        ) as p1
                        )
                / 
                (select count(*)
                from (select distinct player_id
                        from Activity) as p2)
        , 2)
        as fraction
-- @lc code=end

