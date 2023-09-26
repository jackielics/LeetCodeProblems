#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
	def isPalindrome0(self, s: str) -> bool:
		'''
		My Solution0: 0. filter out non-alphanumeric characters 2. compare with reversed string
		'''
		sf = ''.join(filter(str.isalnum, s.lower()))
		return sf == sf[::-1]

	def isPalindrome1(self, s: str) -> bool:
		'''
		My Solution1: two pointers
		'''
		sf = ''.join(filter(str.isalnum, s.lower()))
		l, r = 0, len(sf) - 1
		while l < r:
			if sf[l] != sf[r]:
				return False
			l += 1
			r -= 1
		return True
# @lc code=end