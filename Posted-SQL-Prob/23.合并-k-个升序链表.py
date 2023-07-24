#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		'''
		My Solution0: Recursion, merge 2 linkedlist at one time
		'''
		if len(lists) <= 1: # Recursion Exit: Only 1 elem
			return lists[0] if len(lists) == 1 else None # return head of ListNode
		else: # Recursion Body
			p1 = self.mergeKLists(lists[ : math.ceil(len(lists) // 2)])
			p2 = self.mergeKLists(lists[math.ceil(len(lists) // 2) : ])
			# 假设left和Right已经分别完成排序、合并，开始二合一排序
			p3 = res = ListNode(0) # Dummy node
			while p1 or p2: # at least one not empty
				if not p2 or (p1 and p1.val <= p2.val): # less first
					p3.next = p1 # connect p1-node now
					p1 = p1.next
				elif not p1 or (p2 and p2.val < p1.val): # less first
					p3.next = p2 # connect p1-node now
					p2 = p2.next
				p3 = p3.next # move pointer
			
			return res.next
		
	def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		'''
		My Solution: build a loser tree manually or import heapq
		'''
		

# @lc code=end