#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
	def rob(self, nums: List[int]) -> int:
		'''
		My Solution : O(1) DP
		'''
		if len(nums) <= 2:
			return max(nums)
		
		pprev, prev = 0, 0 # max so far(not necessarily use current )
		for i in range(len(nums)):
			cur = max(prev, pprev + nums[i])
			pprev = prev # move
			prev = cur
		return cur


# @lc code=end