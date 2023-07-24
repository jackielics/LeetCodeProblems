#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		'''
		nums[i] is int, use resMax to record the max product dynamically
		'''
		resMax = float('-inf') # max product
		curMax = curMin = 1 # max/min product in the current string

		for v in nums:
			# right expression will be calculated before left
			curMax, curMin = max(curMin * v, curMax * v, v), min(curMin * v, curMax * v, v)
			resMax = max(resMax, curMax) # update max product
		
		return resMax
# @lc code=end