#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		'''
		My Solution: Front and rear Two pointers
		Time Complexity:O(n)
		Space Complexity:O(1)
		'''
		l, r = 0, len(numbers) - 1
		while l < r:
			if (sumValue := numbers[l] + numbers[r]) == target:
				return [l + 1, r + 1] # return position
			elif sumValue < target:
				l += 1
			else:
				r -= 1
# @lc code=end