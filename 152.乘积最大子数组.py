#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		'''
		ecord the max and min product meanwhile dynamically
		'''
		res = float('-inf') # max product
		curMax = curMin = 1 # max/min product in the current string

		for num in nums:
			# right expression will be calculated before left
			products = (curMin * num, curMax * num, num)
			curMax, curMin = max(products), min(products)
			res = max(res, curMax) # update max product

		return res
# @lc code=end