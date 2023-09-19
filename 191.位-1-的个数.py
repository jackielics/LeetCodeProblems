#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
	def hammingWeight0(self, n: int) -> int:
		s = bin(n)[2:] # Transform dint into bint
		return s.count('1')

	def hammingWeight1(self, n: int) -> int:
		res = 0
		while n:
			res += n % 2
			n //= 2
		return res

	def hammingWeight2(self, n: int) -> int:
		res = 0
		while n:
			n &= (n - 1)
			res += 1
		return res

# @lc code=end

