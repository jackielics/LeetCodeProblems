#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		'''
		1-DP
		'''
		dp = [False] * (len(s) + 1) # if current matches
		dp[0] = True # initial stutas: '' always match
		for i in range(1, len(s) + 1): # start from 1 to len(s)
			for word in wordDict:
				if len(word) <= i: # compare length
					dp[i] = dp[i - len(word)] and s[i - len(word) : i] == word
				if dp[i]: # Once matched, Break
					break
		return dp[-1] # if all string can match
# @lc code=end