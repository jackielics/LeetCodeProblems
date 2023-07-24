#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def kthSmallest0(self, root: Optional[TreeNode], k: int) -> int:
		'''
		My Solution 0: Inorder traversal
		'''
		def recurse(cur)->list:
			# 1 <= k <= n <= 104
			if not cur:
				return []
			
			res = recurse(cur.left) + [cur.val] + recurse(cur.right)
			return res
		
		return recurse(root)[k - 1]

	def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
		'''
		Master's Solution: iterate, use a stack to store NODES
		'''
		i = 0 # index
		stack = []
		cur = root
		while i < k:
			if not cur:
				res = stack.pop() # pop
				i += 1 # numbers of pops
				cur = res.right # move right
			else: # find the less one
				stack.append(cur) # save cur
				cur = cur.left # move left

		return res.val
		
# @lc code=end