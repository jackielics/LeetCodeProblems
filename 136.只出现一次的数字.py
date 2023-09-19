#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
	def singleNumber0(self, nums: List[int]) -> int:
		'''Bit Manipulation ^ Exclusive OR: O(n) O(1)'''
		res = 0
		for v in nums:
			res ^= v #　Exclusive OR
		return res
	
	def singleNumber1(self, nums: List[int]) -> int:
		'''SET'''
		s = set()
		for v in nums:
			if v in s:
				s.remove(v)
			else:
				s.add(v)
		
		return list(s)[0]
# @lc code=end
