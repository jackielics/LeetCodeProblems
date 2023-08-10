#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
	def canJump0(self, nums: List[int]) -> bool:
		'''
		Forward Greedy Strategy
		'''
		cur = 0 # Current Position (Initial)
		far = 0 # Farthest Pos Achievable

		while far < len(nums) - 1 and cur <= far:
			far = max(far, cur + nums[cur]) 
			cur += 1

		if far >= len(nums) - 1:
			return True
		else:
			return False


	def canJump1(self, nums: List[int]) -> bool:
		'''
		Reversed Greedy Strategy
		'''
		Goal = len(nums) - 1
		
		for i in range(len(nums) - 1, -1, -1):
			# [i] reachable => [i-1] reachable
			if i + nums[i] >= Goal:
				Goal = i
		
		if Goal == 0: # Starting Point
			return True
		else:
			return False


# @lc code=end