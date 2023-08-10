#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		'''
		My Solution 0 : Recursion
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		def recurse(root) -> dict:
			'''
			Define a function 
			Return : {'dia':, 'lLen':, 'rLen':}
			'''
			# Recursion exit
			if not root:
				return {'dia':0, 'lLen':-1, 'rLen':-1}
				
			# Recursion body
			left = recurse(root.left)
			right = recurse(root.right)
			left_len = 1 + max(left['lLen'], left['rLen'])
			right_len = 1 + max(right['lLen'], right['rLen'])

			diameter = max(
				left['dia'], 
				right['dia'], 
				left_len + right_len
				)

			return {'dia':diameter, 'lLen':left_len, 'rLen':right_len}
		
		return recurse(root)['dia']

# @lc code=end