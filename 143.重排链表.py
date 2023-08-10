#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		if not head.next or not head.next.next: # 仅一个或两个元素
			return head

		sp, fp = head, head # slow pointer and fast pointer
		while True:# 当fp指向尾节点or空时停止
			sp = sp.next
			fp = fp.next
			if not fp.next: # 记录最后一个节点
				tail = fp
				break
			fp = fp.next
			if not fp.next: # 记录最后一个节点
				tail = fp
				break
		# sp往后的都需要逆转
		prev, cur = None, sp.next # 此时sp指向中间（或偏左）点
		sp.next = None # 让前半段链表的尾结点置空
		while cur:
			nxt = cur.next
			cur.next = prev
			# 前移
			prev = cur
			cur = nxt
		
		# 开始链两接段
		cur = head
		while tail:
			# 存储next节点
			head_nxt = cur.next
			tail_nxt = tail.next
			# 改变指针指向
			cur.next = tail
			tail.next = head_nxt
			# 移动指针
			cur = head_nxt
			tail = tail_nxt

		return head
# @lc code=end

