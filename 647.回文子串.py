#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
	def countSubstrings(self, s: str) -> int:
		'''
		My Solution : DP
		'''
		resCnt = 0 # origin length
		dp = [[False] * len(s)  for _ in range(len(s))]

		for le in range(1, len(s) + 1): # length-of-substring
			for st in range(len(s)): # start-of-substring
				# out-of-bound?
				if (ed := st + le - 1) >= len(s): # end-of-substring
					break
				if s[st] == s[ed]:
					dp[st][ed] = dp[st + 1][ed - 1] if le > 2 else True
					if dp[st][ed]:
						resCnt += 1
		return resCnt
# @lc code=end

