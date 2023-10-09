#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		'''
		2-DP
		'''
		DP = [[0] * n for _ in range(m)] # DP matrix
		DP[0][0] = 1 # initial status: 1 way

		for i in range(m): # rows
			for j in range(n): # cols
				if i > 0:
					DP[i][j] += DP[i - 1][j]
				if j > 0:
					DP[i][j] += DP[i][j - 1]

		return DP[-1][-1]

# @lc code=end