#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
	def maxArea0(self, height: List[int]) -> int:
		'''
		My Solution 0: Brute-force
		Time Complexity: O(n^2)
		Space Complexity: O(1)
		Time Limit Exceeded: 50/61 cases passed (N/A)
		'''
		area = 0
		for i in range(len(height)):
			for j in range(i+1, len(height)):
				area = max(area, min(height[i], height[j]) * (j-i))
		return area
	
	def maxArea1(self, height: List[int]) -> int:
		'''
		My Solution 1: Two Pointers, lesser moves bigger stays
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		area = 0
		l, r = 0, len(height)-1
		while l < r:
			area = max(area, min(height[l], height[r]) * (r-l))
			# move longer -> absulote decrease, move shorter -> may increase
			if height[l] <= height[r]:
				# Move Shorter
				l += 1 
			else:
				r -= 1
		return area
	
# @lc code=end