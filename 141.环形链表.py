#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None

class Solution:
	def hasCycle0(self, head: Optional[ListNode]) -> bool:
		'''
		My Solution: use a DICT to map NODE to index
		'''
		if not head:
			return False # no circle
		node_dict = {}
		p = head # [0,
		while p:
			if node_dict.get(p, None): # new here
				return True # exist a cricle
			else:
				node_dict[p] = 1
			p = p.next
		
		return False

	def hasCycle(self, head: Optional[ListNode]) -> bool:
		'''
		Master's Solution: fast and slow pointer
		'''
		if not head:
			return False
		fast = slow = head
		while slow:
			slow = slow.next
			fast = fast.next
			if not fast or not fast.next: # 以免出现None.next报错的情况
				return False
			fast = fast.next
			if fast == slow: # 速度相差为1，在圆中总会相遇
				return True
		return False
# @lc code=end