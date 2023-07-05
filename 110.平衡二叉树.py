#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isBalanced(self, root: Optional[TreeNode]) -> bool:
		'''
        My Solution 0 : Recursion
		'''
		def dfs_recurse(root)->dict:
			'''
			Return: {depth:int, isBalanced:bool}
			'''
			# Recurison exit
			if not root:
				return {'depth':0, 'isBalanced':True}
			
			left = dfs_recurse(root.left)
			right = dfs_recurse(root.right)
			depth_left = 1 + left.get('depth')
			depth_right = 1 + right.get('depth')

			# minimum-unbalanced-tree appears
			if not (isBalanced := (left.get('isBalanced')
				and right.get('isBalanced')
				and abs(depth_left - depth_right) <=1)):
				return {'depth':-1, 'isBalanced':False} # 

			return {'depth':max(depth_left, depth_right), 'isBalanced':isBalanced}
			
		return dfs_recurse(root).get('isBalanced')

# @lc code=end