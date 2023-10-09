#
# @lc app=leetcode.cn id=440 lang=python3
#
# [440] 字典序的第K小数字
#

# @lc code=start
class Solution:
	def findKthNumber(self, n: int, k: int) -> int:
		nums = [str(x) for x in range(1, n + 1)]
		nums.sort() # asc
		return int(nums[k - 1])

	

# @lc code=end