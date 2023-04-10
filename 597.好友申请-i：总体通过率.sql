--
-- @lc app=leetcode.cn id=597 lang=mysql
--
-- [597] 好友申请 I：总体通过率
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
    ROUND(
        IFNULL(
            (SELECT  COUNT(*)
            FROM 
                (SELECT  requester_id, 
                        accepter_id
                FROM    RequestAccepted
                GROUP BY    requester_id, 
                            accepter_id) AS `T`)
                            /
            (SELECT  COUNT(*)
            FROM 
                (SELECT  sender_id, 
                        send_to_id
                FROM    FriendRequest 
                GROUP BY    sender_id, 
                            send_to_id) AS `T`), 
            0), 
        2) AS `accept_rate`
-- @lc code=end

