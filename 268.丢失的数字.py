#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
	def missingNumber0(self, nums: List[int]) -> int:
		'''
		Brute-Force LIST: O(nlogn), O(1)
		'''
		nums.sort()
		last = -1
		for v in nums:
			if v != last + 1:
				return v - 1
			else:
				last = v
		return v + 1 # n

	def missingNumber1(self, nums: List[int]) -> int:
		'''
		Brute-Force SET: O(n), O(n)
		'''
		s = set(nums)
		for i in range(1 + len(nums)):
			if i not in s:
				return i

	def missingNumber2(self, nums: List[int]) -> int:
		'''Sum Minus'''
		res = len(nums)

		for i in range(len(nums) - 1):
			res += (nums[i] - i)
		return res

	def missingNumber3(self, nums: List[int]) -> int:
		'''Bit Manipulation: Exclusive OR ^'''
		res = len(nums)
		for i in range(len(nums)):
			res ^= nums[i] ^ i
		return res
# @lc code=end