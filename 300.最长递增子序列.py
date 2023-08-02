#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		'''
		1-DP
		'''
		res = 1 # max length of Longest-Increasing-Sequence
		LIS = [1] * len(nums) # initial length of Longest-Increasing-Sequence

		for i in range(len(nums) - 1, -1, -1): # reversely iterate
			for j in range(i, len(nums)): # forwardly  iterate
				if nums[i] < nums[j]: # inherit LIS
					LIS[i] = max(LIS[i], 1 + LIS[j])
					res = max(res, LIS[i])

		return res

# @lc code=end