#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
	def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
		'''
		2-DP 
		'''
		# DP Matrix (len(text2) + 1) * (len(text1) + 1)
		DP = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

		# Bottom-Up Dynamic Programming
		for i in range(len(text2) - 1, -1, -1): # Row 
			for j in range(len(text1) - 1, -1, -1): # Col 
				# deliver
				DP[i][j] = max(max(DP[i + 1][j], DP[i][j + 1]), 
								DP[i + 1][j + 1] + (text2[i] == text1[j]))
		return DP[0][0]


	def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
		'''
		Recurse
		'''
		def dfs(ia, ib, cnt):
			'''
			ia: current index of text1 
			ia: current index of text2
			cnt: length of LCS
			'''
			# reach one bound or two 
			if (ia == len(text1) - 1 or ib == len(text2) - 1):
				if text1[ia] == text2[ib]: # match
					return cnt + 1
				elif ia < len(text1) - 1: # dont match
					return dfs(ia + 1, ib, cnt)
				elif ib < len(text2) - 1:
					return dfs(ia, ib + 1, cnt)
				else:
					return cnt
				
			# reach no bound
			if text1[ia] == text2[ib]: # match
				return dfs(ia + 1, ib + 1, cnt + 1)
			else: # dont match, go two directions
				# Go rightwards or downwards
				rightwards = dfs(ia + 1, ib, cnt)
				downwards = dfs(ia, ib + 1, cnt)
				return max(rightwards, downwards)

		return dfs(0, 0, 0)
	
# @lc code=end