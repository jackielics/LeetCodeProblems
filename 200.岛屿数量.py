#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		R, C = len(grid), len(grid[0]) # Num of Rows, Cols
		res = 0 # Num of Islands
		que = [] # que

		# while que or i 
		for i in range(R):
			for j in range(C):
				if grid[i][j] == '1':
					# Que BFS
					res += 1 # New Island
					que = [(i, j)] # que
					while que:
						cur = que.pop(0) # Pop [0]
						x, y = cur[0], cur[1]
						if grid[x][y] == '1':
							grid[x][y] = '0' # Mark Visited
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
# @lc code=end