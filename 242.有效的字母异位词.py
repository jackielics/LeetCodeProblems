#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
	'''
	my solution: sort
	Time:O(nlogn)
	Space:O(n)
	'''
	def isAnagram0(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		return sorted(s) == sorted(t)
	
	'''
	master solution1: hashMap
	'''
	def isAnagram1(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		cntS, cntT = {}, {}
		for i, j in zip(s, t):
			# get(key, default) return the value of key, if key is not in the dict, return default
			cntS[i], cntT[j] = cntS.get(i, 0) + 1, cntT.get(j, 0) + 1 
		return cntS == cntT
	
	'''
	Master Solution2: use Python Counter
	'''
	def isAnagram(self, s: str, t: str) -> bool:
		return Counter(s) == Counter(t)
# @lc code=end