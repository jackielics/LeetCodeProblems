#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
	def reverseBits0(self, n: int) -> int:
		# Brute-Force
		bs = bin(n)[2:].rjust(32, '0')
		return int(bs[::-1], base = 2)

	def reverseBits(self, n: int) -> int:
		res = 0
		# Get Single Bit
		for i in range(32):
			bit = (n >> i) & 1 # bit[0/1]
			res += (bit << (31 - i))
		return res
# @lc code=end

