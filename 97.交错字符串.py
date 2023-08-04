#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
	def isInterleave0(self, s1: str, s2: str, s3: str) -> bool:
		'''
		Caching-DFS-DP
		'''
		if s3 == s1 + s2: # case: empty string
			return True
		elif len(s3) != len(s1) + len(s2):
			return False

		DP = {(len(s1), len(s2)): True} # {(p1, p2): bool}

		def dfs(p1, p2)->bool:
			res = False
			p3 = p1 + p2
			# Match s1[p1]
			if p1 < len(s1) and s1[p1] == s3[p3]:
				if (p1 + 1, p2) not in DP:
					DP[(p1 + 1, p2)] = dfs(p1 + 1, p2)
				res = res or DP[(p1 + 1, p2)]
			# Match s2[p2]
			if p2 < len(s2) and s2[p2] == s3[p3]:
				if (p1, p2 + 1) not in DP:
					DP[(p1, p2 + 1)] = dfs(p1, p2 + 1)
				res = res or DP[(p1, p2 + 1)]

			DP[(p1, p2)] = res
			return res

		return dfs(0, 0)
	
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		'''
		2-DP
		'''
		if s3 == s1 + s2: # case: empty string
			return True
		elif len(s3) != len(s1) + len(s2):
			return False

		# col_len: len(s1) + 1,		row_len: len(s2) + 1)
		DP = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]

		for r in range(len(s2) + 1): # row, s2
			for c in range(len(s1) + 1): # col, s1
				if r + c == 0:
					DP[r][c] = True # 0, 0
					continue
				i1, i2 = c - 1, r - 1 # current index of s1 and s2
				cur = s3[i1 + i2 + 1] # current char in s3

				# Spread from left to right between cols, try s1[j]
				if c > 0 and DP[r][c - 1]:
					DP[r][c] = DP[r][c] or (cur == s1[i1])
				# Spread from up to down between rows, try s2[i]
				if r > 0 and DP[r - 1][c]:
					DP[r][c] = DP[r][c] or (cur == s2[i2])

		return DP[-1][-1]
# @lc code=end