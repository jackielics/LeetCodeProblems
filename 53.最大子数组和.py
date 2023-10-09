#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# @lc code=start
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		'''
		1-Dynamic Programming or Greedy
		'''
		PreSum = 0
		res = max(nums)
		for v in nums:
			# Greedy: If < 0 then reset to Zero
			PreSum = max(PreSum, 0)
			PreSum += v
			res = max(res, PreSum)
		return res
# @lc code=end

