#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxDepth0(self, root: Optional[TreeNode]) -> int:
		'''
        My Solution 0: Recursion
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		# Recursion exit
		if not root:
			return 0
		
		# Recursion body
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

	def maxDepth1(self, root: Optional[TreeNode]) -> int:
		'''Iterative way'''
		stack = [(root, 1)] # [(node, depth)]
		res = 0

		while stack:
			cur, dep = stack.pop()
			if cur:
				# append left and right subtree with depth
				stack.append((cur.left, dep + 1))
				stack.append((cur.right, dep + 1))
				res = max(res, dep) # update max depth

		return res
# @lc code=end