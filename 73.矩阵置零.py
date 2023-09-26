#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
	def setZeroes0(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# Space Complexity: O(m+n)
		m, n = len(matrix), len(matrix[0])
		rows, cols = set(), set()

		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					rows.add(i)
					cols.add(j)

		for i in range(m):
			for j in range(n):
				if i in rows or j in cols:
					matrix[i][j] = 0

	def setZeroes(self, matrix: List[List[int]]) -> None:
		# Space Complexity: O(1)

		R, C = len(matrix), len(matrix[0])
		row_zero = False

		# use [r][0] as indicator of zero-flag of current row
		for i in range(R):
			for j in range(C):
				if matrix[i][j] == 0:
					matrix[0][j] = 0 # set all cols in row[0]
					# row[0] becomes the indicator of is-zero of all cols
					if i > 0: # set all rows other than row[0] in col[0]
						matrix[i][0] = 0
						# col[0]: indicator of is-zero of all rows except row[0]↓
					else:
						# if [0][] set to zero
						row_zero = True
						# row_zero: indicator of is-zero of row[0]

		# change value of [1,][1,] by row[0][] and col[0][1,]
		for i in range(1, R):
			for j in range(1, C):
				if matrix[0][j] == 0 or matrix[i][0] == 0:
					matrix[i][j] = 0

		# change value of col[0] by the unmodified matrix[0][0] solely
		if matrix[0][0] == 0:
			for i in range(R):
				matrix[i][0] = 0

		# change value of row[0] by the row_zero which representing row[0] will be all-zero
		if row_zero:
			for j in range(C):
				matrix[0][j] = 0
# @lc code=end

