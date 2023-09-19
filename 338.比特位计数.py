#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
	def hammingWeight(self, n: int) -> int:
		res = 0
		while n:
			n &= (n - 1)
			res += 1
		return res

	def countBits0(self, n: int) -> List[int]:
		'''
		nlog2n
		'''
		res = []
		for i in range(n + 1):
			res.append(self.hammingWeight(i))
		return res
	
	def countBits(self, n: int) -> List[int]:
		'''
		1-DP, Bit Munipulation
		'''
		if n == 0:
			return [0]
		elif n == 1:
			return [0, 1]

		dp = [0, 1]
		e = 0 # exponent start from 0

		for i in range(2, n + 1):
			if i == 2**(e + 1): # Jumping Point
				e += 1 # Update e
				dp.append(1)
			else:
				dp.append(1 + dp[i - 2**(e)])
		return dp 
# @lc code=end