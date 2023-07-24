#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		'''
		My Solution:前后双指针法,不知道会不会错过正确答案
		Time Complexity:O(n)
		Space Complexity:O(1)
		'''
		l, r = 0, len(numbers) - 1
		while l < r:
			if numbers[l] + numbers[r] == target:
				return [l + 1, r + 1] # return position
			elif numbers[l] + numbers[r] < target:
				l += 1
			else:
				r -= 1
# @lc code=end