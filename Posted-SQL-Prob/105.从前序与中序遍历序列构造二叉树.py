#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def buildTree0(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		'''
        My Solution 0: recurse according to pattern
		'''
		if len(inorder) == 0:
			return None
		
		for i in range(len(preorder)):
			if preorder[i] in inorder:
				i1 = i # the first preorder NODE in inorder
				i2 = inorder.index(preorder[i])
				break

		# separate into 2 parts according to inorder[i2]
		return TreeNode(preorder[i1], 
			self.buildTree(preorder[i1:], inorder[:i2]), 
			self.buildTree(preorder[i1:], inorder[i2 + 1:]))

	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		'''
        Master's Solution 1: preorder:root->left->right   inorder:left->root->right   
		'''
		if not inorder : # empty list
			return None
		
		m = inorder.index(preorder[0]) # mid 
		# separate into 2 parts by mid
		return TreeNode(preorder[0], 
			self.buildTree(preorder[1 : 1 + m], inorder[:m]), # left: m
			self.buildTree(preorder[m + 1:], inorder[m + 1:]))

# @lc code=end