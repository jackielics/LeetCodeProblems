#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isValidBST0(self, root: Optional[TreeNode]) -> bool:
		'''
		My Solution: Recursion, record minValue and maxValue in subtree
		'''

		def recurse(root, leftChosen = True)->dict:
			'''
			return: {'max': ,'min': , 'bst':}
			'''
			if root.left:
				left = recurse(root.left, True)

				# inequality appears
				if not left['bst']:
					return {'max':None,
	     					'min':None,
						    'bst':False
								}
				left_less = left['max'] < root.val
			else: # no left
				left = {'max':root.val, 'min':root.val, 'bst' : True}
				left_less = True
			
			if root.right:
				right = recurse(root.right, False)

				# inequality appears
				if not right['bst']:
					return {'max':None,
	     					'min':None,
						    'bst':False
								}
				right_more = right['min'] > root.val
			else:
				right = {'max':root.val, 'min':root.val, 'bst' : True}
				right_more = True

			if left['bst'] and right['bst']:
				# leftSub Tree and rightSub Tree are ValidBST
				return {'max': right['max'],
						'min': left['min'],
	    				'bst' 	: 	left_less and right_more}
			else:
				# leftSub Tree and rightSub Tree aren't ValidBST
				return {'max': None,
						'min': None,
	    				'bst' : False}

		return recurse(root)['bst']


	def isValidBST1(self, root: Optional[TreeNode], leftV = float('-inf'), rightV = float('inf')) -> bool:
		'''
		Master's Solution: Recursion, record the boundary
		cur: current node 
		lv: left min value
		rv: right max value
		return: isValidBST or not
		'''
		if not root:
			return True			

		if leftV < root.val < rightV: # satisfied
			return self.isValidBST(root.left, leftV, root.val) and self.isValidBST(root.right, root.val, rightV)
		else: # not satisfied
			return False
		

# @lc code=end