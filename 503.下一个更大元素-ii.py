#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
	def nextGreaterElements(self, nums: List[int]) -> List[int]:
		res = [-1] * len(nums) # fill with -1 initially
		stack = [] # Monotonic Stack[(i, v)]
		for i in range(2 * len(nums)):
			i = i if i < len(nums) else i - len(nums) # reset index
			# pop all elems smaller than V
			while stack and nums[i] > stack[-1]['v']: # not empty, pop out
				pop = stack.pop()
				if res[pop['i']] == -1: # not filled with acutal value
					res[pop['i']] = nums[i] # fill res with actual value
			stack.append({'i':i, 'v':nums[i]}) # push new elem in anyways
		
		return res
# @lc code=end