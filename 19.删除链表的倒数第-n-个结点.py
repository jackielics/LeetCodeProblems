#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		'''
		Master's Solution: use 2-pointers
		'''
		l = r = head
		prev = None # prev is on the left of l
		while n > 1:
			prev = r
			r = r.next
			n -= 1

		if not r.next: # 如果已经到达尾结点
			return head.next # 说明删除的是头结点
		
		while r.next: # r到达尾结点时停止
			prev = l
			l = l.next
			r = r.next

		# 调整指针
		prev.next = l.next
		return head

# @lc code=end

