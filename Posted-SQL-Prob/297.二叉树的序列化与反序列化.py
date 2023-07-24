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
    My Solution 0: BFS, levelOrder, treat it as Full-Binary-Tree    
	'''
	def serialize(self, root):

		# def bfs(cur)->str:
		data = ""
		que = collections.deque()
		que.append(root)
		while que:
			pop = que.popleft()
			if pop:
				data += str(pop.val) + '|'
				que.append(pop.left)
				que.append(pop.right)
			else: # dont append if None
				data += 'null|' # | represents None

		return data


	def deserialize(self, data_str):
		"""
		https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-
		"""
		# turn str to LIST of NODES, but index is not reliable
		data = [TreeNode(int(x)) if x !='null' else None for x in data_str.split('|')[:-1]]
		root = data[0]
		data_que = collections.deque(data)
		del data
		
		# nodes that have already connected to parent but not children yet
		node_que = collections.deque()
		node_que.append(data_que.popleft())

		while data_que:
			pop = node_que.popleft()
			if pop: # skip None
				if data_que:
					pop.left = data_que[0]
					node_que.append(data_que.popleft())

				if data_que:
					pop.right = data_que[0]
					node_que.append(data_que.popleft())

		return root
        
# @lc code=end

