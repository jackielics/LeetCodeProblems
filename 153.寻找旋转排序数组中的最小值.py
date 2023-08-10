#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
	def findMin0(self, nums: List[int]) -> int:
		'''
		My Solution: use min() function in Python
		Time Complexity:	O(N)
		Space Complexity: 	O(1)
		'''
		return min(nums)

	def findMin1(self, nums: List[int]) -> int:
		'''
		My Solution: enhanced binary search
		Time Complexity:	O(logn)
		Space Complexity: 	O(1)
		'''
		l, r = 0, len(nums) - 1
		while l <= r: # find the boundary
			m = (l + r) // 2
			# m是否存在左元素和右元素
			if m > 0 and nums[m - 1] > nums[m]: # 左边大
				return nums[m]
			elif m < (len(nums) - 1) and nums[m + 1] < nums[m]: # 右边小
				return nums[m + 1]

			if nums[l] <= nums[m] <= nums[r]:
				return nums[l] # already sorted
			elif nums[m] < nums[r]:
				r = m - 1
			elif nums[m] > nums[l]:
				l = m + 1
		

# @lc code=end

