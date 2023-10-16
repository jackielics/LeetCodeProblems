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
		nodeToCopy = {} # Mapping: {OldNode: NewNode}

		def dfs(orgNode):
			# Recursion Exit
			if orgNode in nodeToCopy: # Mapped Before
				return nodeToCopy[orgNode]

			# Recursion Body
			newNode = Node(orgNode.val) # Copy
			nodeToCopy[orgNode] = newNode # Mapping
			for nd in orgNode.neighbors: # Connect
				newNode.neighbors.append(dfs(nd))
			
			return newNode
		
		return dfs(node) if node else None
# @lc code=end

