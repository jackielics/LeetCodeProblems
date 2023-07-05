#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		'''
        My Solution 0: recurse, calc maxlen in left and right tree
		'''
		def recurse(cur)->list:
			'''
			Return: [maxLen including curNode, maxLen]
			'''
			if not cur:
				return [float('-inf'), float('-inf')]
			
			Left = recurse(cur.left)
			Right = recurse(cur.right)
			maxCur = max(cur.val, 
				cur.val + Left[0], 
				cur.val + Right[0],
				)

			return [maxCur, 
					max(maxCur, 
						cur.val + Left[0] + Right[0], 
						Left[1], 
						Right[1])]
		
		return recurse(root)[1]

# @lc code=end