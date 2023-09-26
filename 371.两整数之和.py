#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
	def getSum(self, a: int, b: int) -> int:
		# Returns sum of two integers not using +/-

		while(b!=0):
			tmp = (a & b) << 1
			a = a ^ b
			b = tmp

		return a
# @lc code=end