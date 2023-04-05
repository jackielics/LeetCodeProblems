--
-- @lc app=leetcode.cn id=1951 lang=mysql
--
-- [1951] 查询具有最多共同关注者的所有两两结对组
--

-- @lc code=start
# Write your MySQL query statement below
with tmp as
(select r1.user_id as 'user1_id', 
    r2.user_id as 'user2_id', 
    r2.follower_id as 'follower_id'
from Relations r1, Relations r2
where r1.follower_id = r2.follower_id
    and r1.user_id < r2.user_id)

/* select user1_id, user2_id
from tmp 
group by user1_id, user2_id 
having count(*) = ( select max(cnt) 
                    from (  select count(*) as cnt 
                            from tmp 
                            group by user1_id, user2_id) as t) */
/* 刷题不看答案，收获减少一半 */
-- @lc code=end

