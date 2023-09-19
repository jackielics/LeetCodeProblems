#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
	def spiralOrder0(self, matrix: List[List[int]]) -> List[int]:
		'''DFS Recursion'''
		M, N = len(matrix), len(matrix[0])
		res = []

		def judge(i, j, dr):
			# Return True if Accessible
			if dr == 'r':
				return j + 1 < N and matrix[i][j + 1] != 'vst'
			elif dr == 'd':
				return i + 1 < M and matrix[i + 1][j] != 'vst'
			elif dr == 'l':
				return j - 1 > -1 and matrix[i][j - 1] != 'vst'
			elif dr == 'u':
				return i - 1 > -1 and matrix[i - 1][j] != 'vst'

		def dfs(i, j, dr):
			res.append(matrix[i][j])
			matrix[i][j] = 'vst' # Mark Visited
			if dr == 'r': # Right
				# Within Boundary & Not Visited
				if judge(i, j, dr):
					dfs(i, j + 1, 'r') # Keep Right
				elif judge(i, j, 'd'):
					dfs(i + 1, j, 'd') # Turn Down
				else:
					return
			elif dr == 'd': # Down
				if judge(i, j, dr):
					dfs(i + 1, j, 'd') # Keep Down
				elif judge(i, j, 'l'):
					dfs(i, j - 1, 'l') # Turn Left
				else:
					return
			elif dr == 'l': # left
				if judge(i, j, dr):
					dfs(i, j - 1, 'l') # Keep Left
				elif judge(i, j, 'u'):
					dfs(i - 1, j, 'u') # Turn Up
				else:
					return
			elif dr == 'u': # Up
				if judge(i, j, dr):
					dfs(i - 1, j, 'u') # Keep Left
				elif judge(i, j, 'r'):
					dfs(i, j + 1, 'r') # Turn Right
				else:
					return

		dfs(0, 0, 'r') # Start From (0, 0)
		return res
	
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		'''Math Geometry'''
		# Four Pointers: Left, Right, Top, Bottom
		L, R, T, B = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
		res = []

		while L <= R:
			
			# 1st: Right
			for i in range(L, R + 1):
				res.append(matrix[T][i])
			T += 1 # Move `Top`

			if T > B:
				break

			# 2nd: Down
			for i in range(T, B + 1):
				res.append(matrix[i][R])
			R -= 1 # Move `Right`

			if L > R:
				break

			# 3rd: Left
			for i in range(R, L - 1, -1):
				res.append(matrix[B][i])
			B -= 1 # Move `Bottom`
			
			if T > B:
				break

			# 4th: Up
			for i in range(B, T - 1, -1):
				res.append(matrix[i][L])
			L += 1 # Move `Left`

		return res
# @lc code=end