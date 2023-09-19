#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
	def cloneGraph(self, node: 'Node') -> 'Node':
		'''
		DFS Cloning
		'''
		nodeToCopy = {} # {OldNode: NewNode}

		def dfs(node):
			if node in nodeToCopy:
				return nodeToCopy[node]
			
			newNode = Node(node.val) # Reference
			nodeToCopy[node] = newNode
			for nd in node.neighbors:
				newNode.neighbors.append(dfs(nd))
			return newNode
		
		return dfs(node) if node else None
# @lc code=end

