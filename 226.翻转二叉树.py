#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def invertTree0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		'''
        My Solution 0: Recursion
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		# recurison exit
		if not root:
			return None
		# recursion body: swap left and right tree
		left, right = root.left, root.right # store it first
		
		root.left = self.invertTree(right)
		root.right = self.invertTree(left)

		return root 
	
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		'''
        My Solution 1: Recursion
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		# recurison exit
		if not root:
			return None
		# recursion body: swap left and right tree
		root.right, root.left = root.left, root.right # store it first

		self.invertTree(root.left)
		self.invertTree(root.right)

		return root 
# @lc code=end