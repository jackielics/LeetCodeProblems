#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
	'''
    My Solution 0: BFS, treat it as Full-Binary-Tree    
	'''
	def serialize(self, root):
		"""Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
		"""
		# def bfs(cur)->str:
		data = ""
		dq = collections.deque()
		dq.append(root)
		while dq:
			pop = dq.popleft()
			if pop:
				data += str(pop)
				dq.append(pop.left)
				dq.append(pop.right)
			else: # dont append if None
				data += '|' # | represents None

		return data


	def deserialize(self, data):
		"""Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
		"""
		dq = collections.deque()
		dq.append(dq.popleft())

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

