#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
	def trap0(self, height: List[int]) -> int:
		'''
		My Solution: min(l,r) - height[i], l/r is the max height of left/right
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		if len(height) <= 2 or max(height) == min(height): 
			return 0
		# max leftwards/rightwards height at cur(include)
		max_left = [height[0]] * len(height)
		max_right = [height[-1]] * len(height)
		
		# calc max_left and max_right
		for i in range(1, len(height)): # start from last two
			max_left[i] = max(max_left[i - 1], height[i])
			max_right[len(height) - 1 - i] = max(max_right[len(height) - i], height[len(height) - 1 - i])

		res = 0
		catch = 0
		for i in range(1, len(height) - 1): # [2, -2]
			if height[i] == height[i - 1]: # adjacent and same height
				res += catch
				continue

			l = max_left[i - 1]
			r = max_right[i + 1]
			# <0 equals to 0
			catch = max(min(l, r) - height[i], 0)
			res += catch
		return res
	

	def trap(self, height: List[int]) -> int:
		'''
		Master's Solution: 1 loop
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		if len(height) <= 2 or max(height) == min(height): 
			return 0
		
		l, r = 0, len(height) - 1 # Left & Right Pointer
		max_left, max_right = height[l], height[r] # Initial Value
		res = 0 # Total amount

		while l < r:
			# Move the shorter
			if max_left <= max_right:
				l += 1 # Update Pointers
				# if `max_left` updated, res += 0(new left highest)
				max_left = max(max_left, height[l])
				res += max_left - height[l]
			else:
				r -= 1
				max_right = max(max_right, height[r])
				res += max_right - height[r]

		return res
	
# @lc code=end