#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
	def search0(self, nums: List[int], target: int) -> int:
		'''
		My Solution0: LIST.index()
		Time Complexity: O(n)
		'''
		try:
			return nums.index(target)
		except Exception as e:
			return -1
		
	def search1(self, nums: List[int], target: int) -> int:
		'''
		My Solution1: Binary Search
		Time Complexity: O(logn)
		'''
		l, r = 0, len(nums) - 1 # n在 [1, 10000]之间
		while l <= r:
			m = (l + r) // 2 # 在其他语言中可能会溢出
			m = l + (r - l) // 2 # 不可能溢出
			if nums[m] == target:
				return m
			elif nums[m] > target:
				r = m - 1
			else:
				l = m + 1
		return -1
# @lc code=end

