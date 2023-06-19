#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution:
	# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
	# 	# only one node
	# 	if head.next == None:
	# 		return head
	# 	p = head
	# 	n = 0 # length
	# 	while p.next != None:
	# 		p = p.next
	# 		n += 1
	# 	p = head
	# 	for _ in range(n//2 if n%2==0 else n//2+1):
	# 		p = p.next
	# 	return p

	# Master's solution1: use list to store all nodes reversely
	# def middleNode(self, head: ListNode) -> ListNode:
	# 	A = [head]
	# 	while A[-1].next: 
	# 		A.append(A[-1].next)
	# 	return A[len(A) // 2] # Needless to judge parity
	
	# Master's solution2: fast and slow pointers
	def middleNode(self, head: ListNode) -> ListNode:
		slow = fast = head # allowed in python
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow
# @lc code=end

