#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
	def checkInclusion0(self, s1: str, s2: str) -> bool:
		'''
		My Solution0: use LIST to store frequency of each character
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

	def checkInclusion1(self, s1: str, s2: str) -> bool:
		'''
		My Solution1: use DICT
		'''
		if len(s1) > len(s2):
			return False
		
		d1, d2 = {}, {} # dict to store each letter's frequency
		
		for i in range(len(s1)):
			d1[s1[i]] = d1.get(s1[i], 0) + 1
			d2[s2[i]] = d2.get(s2[i], 0) + 1
		
		if d1 == d2: # 是否在开头就匹配成功
			return True

		for r in range(len(s1), len(s2)):
			d2[s2[r]] = d2.get(s2[r], 0) + 1
			lp = r - len(s1) # 之前的l左端点
			d2[s2[lp]] -= 1
			if d2[s2[lp]] == 0: # 删除值为0的键值对
				d2.pop(s2[lp]) 
			if d2 == d1:
				return True
		
		return False

# @lc code=end

