#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		max_idx = len(matrix) - 1 # Max Index in this Square
		# Left and Right Boundary of the Quarter
		l, r = 0, max_idx

		while l < r:
			layer = l # current layer number from the outside to inside
			for offset in range(l, r): # i: offset in cols
				tmp = matrix[layer][offset] # Save Temporarily

				matrix[layer][offset] = matrix[max_idx - offset][layer]

				matrix[max_idx - offset][layer] = matrix[max_idx - layer][max_idx - offset]

				matrix[max_idx - layer][max_idx - offset] = matrix[offset][max_idx - layer]

				matrix[offset][max_idx - layer] = tmp

			l += 1
			r -= 1

# @lc code=end

