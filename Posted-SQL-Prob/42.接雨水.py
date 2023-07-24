#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
	def trap(self, height: List[int]) -> int:
		'''
		My Solution: min(l,r) - height[i], l/r is the max height of left/right
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		if len(height) <= 2 or max(height) == min(height): 
			return 0
		
		max_left = [height[0]] * len(height) # max height from left
		max_right = [height[-1]] * len(height)
		for i in range(1, len(height)):
			max_left[i] = max(max_left[i - 1], height[i])
			max_right[len(height) - i - 1] = max(max_right[len(height) - i], height[len(height) - i - 1])

		res = 0
		tmp = 0
		for i in range(1, len(height) - 1):
			if i > 0 and height[i] == height[i - 1]: # adjacent and same height
				res += tmp
				continue

			# boundary equals to 0
			l = max_left[i - 1] if i > 0 else 0
			r = max_right[i + 1] if i < len(height) - 1 else 0
			# <0 equals to 0
			tmp = max(min(l, r) - height[i], 0)
			res += tmp
		return res
	

	def trap1(self, height: List[int]) -> int:
		'''
		Master's Solution: 1 loop
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		if len(height) <= 2 or max(height) == min(height): 
			return 0
		
		# max_left = [height[0]] * len(height) # max height from left
		# max_right = [height[-1]] * len(height)
		# for i in range(1, len(height)):
		# 	max_left[i] = max(max_left[i - 1], height[i])
		# 	max_right[len(height) - i - 1] = max(max_right[len(height) - i], height[len(height) - i - 1])

		res = 0
		tmp = 0
		ml, mr = height[0], height[-1]
		for i in range(1, len(height) - 1): # no boundaries
			if height[i] == height[i - 1]: # adjacent and same height
				res += tmp
				continue
				
			ml, mr = max(ml, height[i - 1]), max(mr, height[len(height) - i - 1])
			
			l = max_left[i - 1]
			r = max_right[i + 1]
			# <0 equals to 0
			tmp = max(min(l, r) - height[i], 0)
			res += tmp
		return res
# @lc code=end