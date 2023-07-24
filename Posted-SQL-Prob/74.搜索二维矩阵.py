#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
	def searchMatrix0(self, matrix: List[List[int]], target: int) -> bool:
		'''
		My Solution: 取m时向上对齐
		Time Complexity: 	O(log(mn))
		Space COmplexity:	O(1)
		'''
		# 找行
		l, r = 0, len(matrix) - 1
		while l < r: # 对齐时退出
			m = math.ceil(l + (r - l) / 2) # 向上取整
			if target > matrix[m][0]:
				l = m
			elif target < matrix[m][0]:
				r = m - 1
			else: # 正好等于
				return True
		i = l

		l, r = 0, len(matrix[i]) - 1

		# 找列
		while l <= r: # l > r时退出
			m = math.ceil(l + (r - l) / 2) # 向上取整
			if target > matrix[i][m]:
				l = m + 1
			elif target < matrix[i][m]:
				r = m - 1
			else: # 正好等于
				return True
		
		return False
	
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		'''
		Master Solution: use Numpy.reshape 
		'''
		import numpy as np
		return target in np.reshape(matrix, -1)

# @lc code=end

