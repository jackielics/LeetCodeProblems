#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reverseList0(self, head: Optional[ListNode]) -> Optional[ListNode]:
		'''
		My Solution0: iterate
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		if not head or not head.next: # 对于空or只有头结点的，返回自身
			return head
		prev, cur = head, head.next
		prev.next = None
		while cur:
			nxt = cur.next # save next.next
			cur.next = prev # change pointer
			prev, cur = cur, nxt
		return prev
	
# @lc code=end