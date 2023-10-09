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
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''
		My Solution 0: DFS, recursion, for generic binary-tree
		Time Complexity: O(logn)
		Space Complexity: O(1)
		'''
		def recurse(cur)->dict:
			'''
			Return: {'p':, 'q':, 'lca':}
			'''
			# Recursion Exit
			if not cur:
				return {} # 
			
			# Recursion Body
			res = {**recurse(cur.left), **recurse(cur.right)}
			if cur == p:
				res.update({'p' : cur})
			elif cur == q:
				res.update({'q' : cur})
			# record the Lowest Common Ancestor
			if len(res) == 2: # p&q, no lca
				res.update({'lca' : cur})

			return res

		return recurse(root)['lca']
	
	def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''
		Master's Solution: designed for BST
		'''
		while True:
			# p and q both > root.val
			if min(p.val, q.val) > root.val:
				root = root.right
			# p and q both < root.val
			elif max(p.val, q.val) < root.val:
				root = root.left
			else: # p < root < q
				return root
# @lc code=end