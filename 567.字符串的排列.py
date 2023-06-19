#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		'''
		s1 = "ab" 
		s2 = "eidbaooo"
		'''
		if len(s1) > len(s2):
			return False
		s1Count, s2Count = [0] * 26, [0] * 26
		# [0, len(s1)-1]
		for i in range(len(s1)):
			# ord() 函数：返回对应字符的 ASCII 数值，或者 Unicode 数值
			# Building Hashmap
			s1Count[ord(s1[i]) - ord('a')] += 1
			s2Count[ord(s2[i]) - ord('a')] += 1
		
		matches = 0 # number of matched letters
		for i in range(26):
			matches += (1 if s1Count[i] == s2Count[i] else 0)
		# [len(s1), len(s2)-1]
		for r in range(len(s1), len(s2)):
			if matches == 26: # matches perfectly
				return True
			
			pos = ord(s2[r]) - ord('a') # upcoming letter
			s2Count[pos] += 1
			if s1Count[pos] == s2Count[pos]:
				matches += 1
			# not equal anymore after adding one
			elif s1Count[pos] + 1 == s2Count[pos]: 
				matches -= 1
			
			l = r - len(s1)
			pos = ord(s2[l]) - ord('a') # leaving letter
			s2Count[pos] -= 1
			if s1Count[pos] == s2Count[pos]: # 
				matches += 1
			# not equal anymore after subtracting one
			elif s1Count[pos] - 1 == s2Count[pos]:
				matches -= 1
			
		return matches == 26

# Reference: https://www.youtube.com/watch?v=UbyhOgBN834
# @lc code=end

