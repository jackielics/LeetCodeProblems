#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
	def climbStairs(self, n: int) -> int:
		'''
		DP
		res[i] = res[i-1] + res[i-2]
		'''
		if n == 1:
			return 1
		elif  n == 2:
			return 2

		res = [1, 1] + [1] * (n - 1)
		for i in range(2, n + 1):
			res[i] = res[i - 2] + res[i - 1]
		
		return res[n]

	def climbStairs1(self, n: int) -> int:
		'''
		DP using least memory 
		'''
		if n <= 2: # 1-1, 2-2
			return n

		pp, p = 1, 2 # prev's prev, prev
		for _ in range(2, n):
			# res[i] = res[i - 2] + res[i - 1]
			cur = pp + p
			pp = p # move
			p = cur
		
		return cur
	
	def climbStairs2(self, n: int) -> int:
		'''
		recurse, but Exceeded
		'''
		if n == 1:
			return 1
		elif  n == 2:
			return 2
		return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# @lc code=end