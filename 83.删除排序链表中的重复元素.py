#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            nxt = cur.next
            if nxt and cur.val == nxt.val: # Skip
                cur.next = nxt.next
                nxt = nxt.next
            else: # Move
                cur = nxt
        return head
# @lc code=end

