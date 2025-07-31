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
		root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

		return root 

	def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		'''
		Stack
		'''
		if not root:
			return None
		stack = [root]

		while stack:
			curNode = stack.pop()
			if curNode.left:
				stack.append(curNode.left)
			if curNode.right:
				stack.append(curNode.right)
			curNode.left, curNode.right = curNode.right, curNode.left
		return root

# @lc code=end