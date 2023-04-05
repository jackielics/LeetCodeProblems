--
-- @lc app=leetcode.cn id=1949 lang=mysql
--
-- [1949] 坚定的友谊
--

-- @lc code=start
# Write your MySQL query statement below


with
    # 找出单向的所有朋友关系
    friends as
    (select user1_id as 'people', user2_id as 'make_friend_with'
    from Friendship f
    union all
    select user2_id as 'people', user1_id as 'make_friend_with'
    from Friendship f), 
    # 找出交到同一个朋友的两个人
    common_friends_table as
    (select  f1.people as 'user1_id', f2.people as 'user2_id', f1.make_friend_with
    from    friends f1, friends f2
    where   f1.people < f2.people
        and f1.make_friend_with = f2.make_friend_with)


select  f.user1_id, f.user2_id, count(*) as 'common_friend'
from    common_friends_table c
right join Friendship f # 避免本身不是朋友却有共同朋友的情况
on      c.user1_id = f.user1_id
    and c.user2_id = f.user2_id
group by    f.user1_id, f.user2_id
having count(*) >= 3



-- @lc code=end

