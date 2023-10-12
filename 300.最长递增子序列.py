#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
	def lengthOfLIS0(self, nums: List[int]) -> int:
		'''1-DP'''
		res = 1 # max length of Longest-Increasing-Sequence
		DP = [1] * len(nums) # initial length of Longest-Increasing-Sequence
		for i in range(len(nums)): # iterate
			for j in range(i): # [0, i-1] -> i
				if nums[i] > nums[j]: # Strictly increasing
					DP[i] = max(DP[i], 1 + DP[j])
					res = max(res, DP[i])
		return res

	def lengthOfLIS1(self, nums: List[int]) -> int:
		'''Reversed 1-DP'''
		res = 1 # max length of Longest-Increasing-Sequence
		DP = [1] * len(nums) # initial length of Longest-Increasing-Sequence

		for i in range(len(nums) - 1, -1, -1): # reversely iterate
			for j in range(i, len(nums)): # forwardly  iterate
				if nums[i] < nums[j]: # inherit LIS
					DP[i] = max(DP[i], 1 + DP[j])
					res = max(res, DP[i])
		return res
	
	def lengthOfLIS(self, nums: [int]) -> int:
		'''Binary Search'''
		increase = [0] * len(nums)
		res = 0 # max length of increasing subquence
		for num in nums:
			l, r = 0, res
			while l < r:
				m = (l + r) // 2
				if num > increase[m]:
					l = m + 1
				else: # num >= increase[m]
					r = m # [r] is the last (increase[m] <= num)
			increase[l] = num # num > increase[:l] strictly increase
			# if r(index, start from 0) == res(length, start from 1) 
			if r == res: # no increase[i] <= num
				res += 1
		return res

# @lc code=end