#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
	def search0(self, nums: List[int], target: int) -> int:
		'''
		My Solution0: use LIST.index 
		'''
		if target in nums:
			return nums.index(target)
		else:
			return -1

	def search1(self, nums: List[int], target: int) -> int:
		'''
		My Solution: 1. find the boundary index 2. binary-search
		'''
		v0 = nums[0]
		l, r = 0, len(nums) - 1
		while l <= r: # find the boundary
			m = (l + r) // 2
			# m是否存在左元素和右元素
			if m > 0 and nums[m - 1] > nums[m]: # 左边大
				# return nums[m]
				start = m
				break
			elif m < (len(nums) - 1) and nums[m + 1] < nums[m]: # 右边小
				start = m + 1
				break
			if nums[l] <= nums[m] <= nums[r]: # already sorted
				start = l
				break
			elif nums[m] < nums[r]:
				r = m - 1
			elif nums[m] > nums[l]:
				l = m + 1

		nums2 = nums[start:] + nums[:start]
		l, r = 0, len(nums2) - 1
		while l <= r:
			m = (l + r) // 2
			if nums2[m] == target:
				return (m + start if target < v0 else (m + start) % len(nums))
			elif nums2[m] > target:
				r = m - 1
			else:
				l = m + 1
		return -1
	
	def search2(self, nums: List[int], target: int) -> int:
		'''
		
		'''
		l, r = 0, len(nums) - 1
		while l <= r:
			m = (l + r) // 2
			if nums[m] == target: # found
				return m
			# sorted sequence condition is aslo considered
			elif nums[m] >= nums[l]: # on the left
				if nums[m] > target >= nums[l]: # to the left
					r = m - 1
					pass
				else: # to the left
					l = m + 1
					pass
			elif nums[m] <= nums[r]: # on the right
				if nums[m] < target <= nums[r]:
					l = m + 1
					pass
				else:
					r = m - 1
					pass

		return -1 # not found
# @lc code=end