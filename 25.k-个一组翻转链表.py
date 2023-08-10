#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		'''
		
		'''
		r = head # initialize right pointer
		l_old = None
		while r:
			
			l = r # update l pointer
			for _ in range(k): # move right pointer
				# TODO: what if r is None
				if not r:
					# connect current to the last sequence
					l_old.next = l
					return newHead
				r = r.next # r: the start of next string
			
			cur = l # change cur's next pointer
			prev = None # 1st pointer(l) to None
			while cur != r:
				# reverse pointer
				nxt = cur.next # store next
				cur.next = prev # connect current to the prev

				prev = cur # update prev
				cur = nxt # update cur

			if l == head: # 1st sequence
				newHead = prev # record head

			# connect current sequence to the last sequence
			if l_old:
				l_old.next = prev

			l_old = l # record 

		return newHead

# @lc code=end