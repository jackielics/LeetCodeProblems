#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		'''
        My Solution 0: BFS, iterate by collections.deque()
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		if not root:
			return []
		deque = collections.deque()
		# population: [0, 2000]
		res = []
		deque.append([root])
		while deque:
			cur = deque.popleft()
			val = [] # value list
			node = [] # node list
			for v in cur:
				val.append(v.val)
				# don't add None
				if v.left:
					node.append(v.left)
				if v.right:
					node.append(v.right)
			if node: # dont add []
				deque.append(node)
			if val:
				res.append(val)
		return res

			
# @lc code=end