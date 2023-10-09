#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
	def rob(self, nums: List[int]) -> int:
		'''
        Master's Sulotion: DP, ignore either first or last one 
		'''
		# 1 <= nums.length <= 100
		if len(nums) <= 3:
			return max(nums)
		
		pp1, p1 = pp2, p2 = 0, 0
		for v1, v2 in zip(nums[1:], nums[:-1]): # ignore first or last
			cur1, cur2 = max(p1, pp1 + v1), max(p2, pp2 + v2)
			pp1, pp2 = p1, p2
			p1, p2 = cur1, cur2
		
		return max(cur1, cur2)
# @lc code=end