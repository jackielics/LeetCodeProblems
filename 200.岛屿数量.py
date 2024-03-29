#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
	def numIslands0(self, grid: List[List[str]]) -> int:
		'''Iteration BFS'''
		R, C = len(grid), len(grid[0]) # Num of Rows, Cols
		res = 0 # Num of Islands
		que = [] # que

		# while que or i 
		for i in range(R):
			for j in range(C):
				if grid[i][j] == '1':
					# List-Que-Based BFS
					res += 1 # New Island
					que = [(i, j)] # que
					while que:
						cur = que.pop(0) # Pop [0]
						x, y = cur[0], cur[1]
						if grid[x][y] == '1':
							grid[x][y] = '0' # Mark Visited by changing value
							# Try Adjacency
							if x > 0 and grid[x - 1][y] == '1':
								que.append((x - 1, y))
							if y > 0 and grid[x][y - 1] == '1':
								que.append((x, y - 1))
							if x < R - 1 and grid[x + 1][y] == '1':
								que.append((x + 1, y))
							if y < C - 1 and grid[x][y + 1] == '1':
								que.append((x, y + 1))

		return res

	def numIslands1(self, grid: List[List[str]]) -> int:
		'''DFS Recursion'''
		res = 0 # Num of Islands
		R, C = len(grid), len(grid[0])
		visited = set() # {(i, j)}

		def dfs(i, j):
			# out-of-bounds || '0' || visited
			if not (-1 < i < R and -1 < j < C) or \
				grid[i][j] == '0' or \
				(i, j) in visited:
				return 
			
			for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
				visited.add((i, j))
				dfs(i + x, j + y)

		for i in range(R):
			for j in range(C):
				if grid[i][j] == '1' and (i, j) not in visited:
					res += 1
					dfs(i, j)

		return res
# @lc code=end