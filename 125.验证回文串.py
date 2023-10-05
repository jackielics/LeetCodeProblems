#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
	def isPalindrome0(self, s: str) -> bool:
		'''
		My Solution0: 
		1. filter out non-alphanumeric characters 
		2. compare with reversed string
		'''
		sf = ''.join(filter(str.isalnum, s.lower()))
		return sf == sf[::-1]

	def isPalindrome(self, s: str) -> bool:
		'''
		My Solution1: Two pointers
		'''
		l, r = 0, len(s) - 1
		while l < r:
			while l < r and not s[l].isalnum():
				l += 1
			while l < r and not s[r].isalnum():
				r -= 1
			if s[l].lower() != s[r].lower():
				return False
			l += 1
			r -= 1
		return True
# @lc code=end