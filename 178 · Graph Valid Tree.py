# https://www.lintcode.com/problem/178/
from typing import (
    List,
)

class Solution:
	"""
	@param n: An integer
	@param edges: a list of undirected edges
	@return: true if it's a valid tree, or false
	"""
	def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
		
		if not edges:
			if n < 2:
				print (True)
			else:
				print (False)

		vst = set()
		graph = {}
		# Build Graph
		graph = {i: [] for i in range(n)}
		for x, y in edges:
			graph[x].append(y)
			graph[y].append(x)

		# start from 0
		def dfs(cur, prev):
			'''
			cur: current node 
			prev: previous node 
			'''
			if cur not in vst:
				vst.add(cur)
				for v in graph[cur]:
					if v != prev:
						if not dfs(v, prev = cur):
							return False
			# visited and not prev
			else:
				return False
			
			return True

		return (dfs(0, 0) and len(vst) == n)