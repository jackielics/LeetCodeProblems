#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
	def fib0(self, n: int) -> int:
		'''Recursion'''
		def recurse(n):
			if n == 0:
				return 0
			elif n == 1:
				return 1
			return recurse(n - 1) + recurse(n - 2)
		return recurse(n)
	
	def fib1(self, n: int) -> int:
		'''1-DP'''
		DP = [0] * (n + 1)
		if n >= 1:
			DP[1] = 1
		for i in range(2, n + 1):
			DP[i] = DP[i - 1] + DP[i - 2]
		return DP[-1]
	
	def fib2(self, n: int) -> int:
		'''caching recurse'''
		cache = {0:0, 1:1}
		def recurse(cur):
			if cur not in cache:
				cache[cur] = recurse(cur - 1) + recurse(cur - 2)
			return cache[cur]
		return recurse(n)
	


# @lc code=end