#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		'''
		Master's Solution: use a LIST to store frequency of each character
		Time Complexity: O(N)
		Space Complexity: O(1)
		'''
		char_freq = [0] * 26 # 0对应A，依此类推

		l, r = 0, 0
		maxFreq = 0
		res = 0

		for r in range(len(s)):
			idx = ord(s[r]) - ord('A')
			subLen = r - l + 1 # length of substring
			char_freq[idx] += 1
			maxFreq = max(maxFreq, 	char_freq[idx]) # 区间扩展时需要更新
			if subLen - maxFreq <= k: # k次变换能够添补断点
				res = max(res, subLen) # 更新结果
			else: # 不够填充，开始削减
				while subLen - maxFreq > k:
					idx = ord(s[l]) - ord('A')
					char_freq[idx] -= 1
					l += 1
					# 区间紧缩时不需要更新 maxFreq
					# 如果减去的s[l]是最大频率的字符，maxFreq会与subLen一同变小，subLen - maxFreq不变
					# 如果减去的s[l]不是最大频率的字符（或者只是最大频率的字符之一），maxFreq不变，subLen变小
					subLen = r - l + 1 # length of substring

		return res
			
		  
# @lc code=end

