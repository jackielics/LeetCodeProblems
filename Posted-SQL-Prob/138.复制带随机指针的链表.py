#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random
"""

class Solution:
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		'''
		Master's Solution: 2-loops, use a DICT to map origin node to the copied node 
		'''
		if not head: # 0 <= n
			return None
		
		origin_to_copy = {}
		p1 = head
		# 复制节点、建立映射
		while p1: # 到尾结点
			p2 = Node(p1.val) # 新加节点
			origin_to_copy[p1] = p2
			p1 = p1.next # p1后移

		# 指针链接
		p1, p2 = head, origin_to_copy[head]
		while p1: # 到尾结点
			p2.next = origin_to_copy[p1.next] if p1.next else None
			p2.random = origin_to_copy[p1.random] if p1.random else None
			p1, p2 = p1.next, p2.next

		return origin_to_copy[head]
	
# @lc code=end

