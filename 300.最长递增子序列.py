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
		'''1-DP reversed'''
		res = 1 # max length of Longest-Increasing-Sequence
		DP = [1] * len(nums) # initial length of Longest-Increasing-Sequence

		for i in range(len(nums) - 1, -1, -1): # reversely iterate
			for j in range(i, len(nums)): # forwardly  iterate
				if nums[i] < nums[j]: # inherit LIS
					DP[i] = max(DP[i], 1 + DP[j])
					res = max(res, DP[i])

		return res
# @lc code=end