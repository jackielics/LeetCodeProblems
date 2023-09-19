# https://www.lintcode.com/problem/3651/

class Solution:
	"""
	@param n: the number of vertices
	@param edges: the edges of undirected graph
	@return: the number of connected components
	"""
	def count_components(self, n: int, edges: List[List[int]]) -> int:
		# write your code here
		res = 0
		graph = {} # {node:[adjs]}

		vst = set() # visited

		for x, y in edges:
			graph[x] = graph.get(x, []) + [y]
			graph[y] = graph.get(y, []) + [x]

		def dfs(cur):
			if cur in vst: 
				return 
			else: 
				vst.add(cur)
				for v in graph[cur]:
					dfs(v)
				return


		for v in range(n):
			if v not in graph:
				res += 1
			elif v not in vst:
				dfs(v)
				res += 1

		return res