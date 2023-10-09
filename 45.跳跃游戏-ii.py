#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
	def jump0(self, nums: List[int]) -> int:
		'''
		Greedy Range Pointer
		'''
		res = 0 # Steps to Reach [-1]
		l = r = 0 # Left and Right Bound of A Continuous Range
		res = 0 # Min Steps Reaching Cur Pos

		while r < len(nums) - 1: # While Didn't Reach End
			far = 0 # Farthest Pos Reachable From [l, r]
			for i in range(l, r + 1): # [l, r]
				far = max(far, i + nums[i])
			l = r + 1
			r = far # update r to the farthest
			res += 1

		return res

	def jump1(self, nums: List[int]) -> int:
		'''
		1-DP
		'''
		cur = 0 # Current Position (Initial)
		far = 0 # Farthest Pos Achievable
		DP = [float('inf')] * len(nums) # Smallest Steps Reaching Index
		DP[0] = 0 # Initial Pos
		while cur < len(nums) - 1:
			far = cur + nums[cur] # Farthest Pos Reachable From Cur
			# [Cur + 1, Farthest]: Reachable; Avoid Out-of-Bounds
			for i in range(cur + 1, min(far + 1, len(nums))): 
				DP[i] = min(DP[i], DP[cur] + 1) # Fetch Smaller Value
			cur += 1 # Move Cur

		return DP[-1]

# @lc code=end