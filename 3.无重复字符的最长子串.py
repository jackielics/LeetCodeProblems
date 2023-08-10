#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
	def lengthOfLongestSubstring0(self, s: str) -> int:
		'''
		My Solution: Sliding Window
		'''
		maxLen = 0
		l = 0
		for r in range(len(s)):
			while (r - l + 1) != len(set(s[l : r + 1])): # 有重复时l右移直到只剩一个字符
				l += 1 # 缩小范围
			maxLen = max(maxLen, r - l + 1)
		return maxLen

	def lengthOfLongestSubstring1(self, s: str) -> int:
		'''
		My Solution1: Dynamic Programming
		'''
		if len(s) == 0:
			return 0
		dp = [0] * len(s) # 到目前为止的不重复字符串最长长度
		l = 0
		for r in range(len(s)):
			while (r - l + 1) != len(set(s[l : r + 1])): # 有重复时l右移直到只剩一个字符
				l += 1 # 缩小范围
			dp[r] = max(dp[r - 1], r - l + 1)
		return dp[-1]

# @lc code=end

