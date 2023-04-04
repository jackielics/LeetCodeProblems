--
-- @lc app=leetcode.cn id=1341 lang=mysql
--
-- [1341] 电影评分
--

-- @lc code=start
# Write your MySQL query statement below
(select u.name as 'results'
from MovieRating m
left join Users u
on m.user_id = u.user_id
group by m.user_id
having count(*) = (
    SELECT MAX(cnt)
    FROM (SELECT COUNT(*) AS cnt
    FROM MovieRating m2
    GROUP BY m2.user_id) AS subquery
)
order by u.name asc 
limit 0,1)
union
(select mv.title as 'results'
from MovieRating mr
left join Movies mv
on mr.movie_id = mv.movie_id
where mr.created_at like '2020-02%'
group by mr.movie_id
having round(avg(mr.rating), 10) = (
    SELECT max(ave)
    FROM (  SELECT AVG(mr2.rating) AS ave
            FROM MovieRating mr2
            where mr2.created_at like '2020-02%'
            GROUP BY mr2.movie_id) AS subquery
)
order by mv.title asc 
limit 0,1
)
-- @lc code=end

