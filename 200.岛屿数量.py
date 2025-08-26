#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
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
			else:
				visited.add((i, j))

			for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
				dfs(i + x, j + y)

		for i in range(R):
			for j in range(C):
				if grid[i][j] == '1' and (i, j) not in visited:
					res += 1
					dfs(i, j)
# @lc code=end