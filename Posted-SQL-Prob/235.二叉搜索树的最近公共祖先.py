#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor0(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''
		My Solution 0: DFS, recursion, for generic binary-tree
		Time Complexity: O(logn)
		Space Complexity: O(1)
		'''
		def recurse(root)->dict:
			'''
			Return: {'p':, 'q':, 'Anc':}
			'''
			# Recursion Exit
			if not root:
				return {} # 
			
			# Recursion Body
			res = {**recurse(root.left), **recurse(root.right)}
			if root == p:
				res.update({'p' : root})
			elif root == q:
				res.update({'q' : root})
			
			# record the first Ancestor
			if len(res) == 2: # p&q, no Anc
				res.update({'Anc' : root})

			return res

		return recurse(root)['Anc']
	
	def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''
		Master's Solution: designed for BST
		'''
		while True:
			if p.val > root.val and q.val > root.val:
				root = root.right
			elif p.val < root.val and q.val < root.val:
				root = root.left
			else: 
				return root
# @lc code=end