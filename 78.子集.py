#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		'''
		use backtrack to cover every possible result
		'''
		res = [] # ret
		subset = [] # record pilot process

		def backtrack(i):
			if i >= len(nums):
				res.append(subset.copy()) # shallow copy
				return

			subset.append(nums[i])
			backtrack(i + 1) # with nums[i]

			subset.pop()
			backtrack(i + 1) # without nums[i]

		backtrack(0) # start from 0

		return res
# @lc code=end