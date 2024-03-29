#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
	def longestCommonSubsequence0(self, text1: str, text2: str) -> int:
		'''2-DP'''
		# DP Matrix (len(text2) + 1) * (len(text1) + 1)
		DP = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

		# Dynamic Programming
		for i in range(1, 1 + len(text2)): # Row 
			for j in range(1, 1 + len(text1)): # Col 
				# Just Inherit from left or above or Try to Compare from diagonal
				DP[i][j] = max(DP[i - 1][j], DP[i][j - 1], 
							DP[i - 1][j - 1] + (text2[i - 1] == text1[j - 1]))
		return DP[-1][-1]

	def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
		'''Recursion: TLE'''
		def dfs(ia, ib, cnt):
			'''
			ia: current index in text1
			ia: current index in text2
			cnt: length of LCS
			'''
			# out of bounds
			if ia >= len(text1) or ib >= len(text2):
				return cnt
			# within bound and match
			elif text1[ia] == text2[ib]: # match
				return dfs(ia + 1, ib + 1, cnt + 1)
			else: # dont match, go two directions
				# Go rightwards or downwards
				rightwards = dfs(ia + 1, ib, cnt)
				downwards = dfs(ia, ib + 1, cnt)
				return max(rightwards, downwards)

		return dfs(0, 0, 0)
# @lc code=end