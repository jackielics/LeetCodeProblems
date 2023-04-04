--
-- @lc app=leetcode.cn id=1264 lang=mysql
--
-- [1264] 页面推荐
--

-- @lc code=start
# Write your MySQL query statement below
select (distinct l.page_id) as recommended_page
from (select case 
        when user1_id = 1 then user2_id 
        when user2_id = 1 then user1_id 
        end as user_id
    from Friendship ) as f, Likes as l
where l.user_id = f.user_id 
    and l.page_id not in (select page_id 
                            from Likes 
                            where user_id = 1)

-- @lc code=end

