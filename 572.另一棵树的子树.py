#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def isSubtree(self, 
	       root: Optional[TreeNode], 
		   subRoot: Optional[TreeNode],
		   adjacent:bool = False) -> bool:
		'''
		adjacenct is adjacency required?
		My Solution 0: Recursion
		Time Complexity: O(n^2)
		Space Complexity: O(n)
		'''
		# Recursion Exit
		if not root and not subRoot:
			return True
		elif not root or not subRoot:
			return False
		
		
		equal = True
		if root.val == subRoot.val: # root matches
			# left and right aslo match
			if self.isSubtree(root.left, subRoot.left, True) and \
				self.isSubtree(root.right, subRoot.right, True):
				# perfectly matches
				return True
			else:
				equal = False
		else:
				equal = False

		# inequal and adjacent
		if not equal and adjacent:
			return False

		# left Subtree or right Subtree matches
		return (self.isSubtree(root.left, subRoot, False) or \
			self.isSubtree(root.right, subRoot, False))

# @lc code=end

