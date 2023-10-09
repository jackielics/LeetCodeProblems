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
		My Solution0: iterate using 3 pointers [prev, cur, next]
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		# For null or only head
		if not head or not head.next: 
			return head
		prev, cur = head, head.next
		prev.next = None
		while cur:
			nxt = cur.next # save next.next
			cur.next = prev # change pointer
			prev, cur = cur, nxt
		return prev
	
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# Recursion: Nested function
		def recurse(cur, prev):
			# reverse cur and prev
			if not cur:
				return prev
			nxt = cur.next
			cur.next = prev
			return recurse(nxt, cur) # Key Point!
		
		return recurse(head, None)
	

# @lc code=end