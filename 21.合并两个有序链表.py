#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		'''
		My Solution: iterate
		'''
		p1, p2 = list1, list2
		if not p1 and not p2:
			return None
		list3 = ListNode(-1) # dummy node
		p3 = list3
		
		while p1 or p2: # 都为空时停止
			if not p2 or (p1 and p1.val <= p2.val): # 如果p2为空orP1不为空且p1<=p2
				p3.next = p1
				p3 = p3.next
				p1 = p1.next
			elif not p1 or (p2 and p2.val < p1.val):
				p3.next = p2
				p3 = p3.next
				p2 = p2.next
				
		return list3.next

	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		'''
		Master's Solution: recursion
		'''
		if not list1: # 递归出口：到达尾部
			return list2 # 其中一个到达尾部，just接另一个
		if not list2:
			return list1

		if list1.val <= list2.val:
			list1.next = self.mergeTwoLists(list1.next, list2)
			return list1
		else:
			list2.next = self.mergeTwoLists(list1, list2.next)
			return list2
		

# @lc code=end

