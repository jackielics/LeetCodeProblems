#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		'''
		DP
		'''
		dp = [False] * (len(s) + 1) # if current matches?
		dp[0] = True # initial stutas
		for i in range(1, len(s) + 1): # start from 1 to len(s)
			for w in wordDict:
				if len(w) <= i: # compare length
					dp[i] = dp[i - len(w)] and s[i - len(w) : i] == w
				if dp[i]: # matched
					break
		return dp[-1]
# @lc code=end