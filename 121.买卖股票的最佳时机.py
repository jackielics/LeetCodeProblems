#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
	def maxProfit0(self, prices: List[int]) -> int:
		'''
		My Solution: just loop
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		res = 0
		# 1 <= prices.length
		minV = prices[0] # 前面的最小值
		# 对于每个数，找之前小于他的值
		for i in range(1, len(prices)):
			profit = prices[i] - minV
			minV = min(minV, prices[i])
			res = max(res, profit)
		return res
	
	def maxProfit1(self, prices: List[int]) -> int:
		'''
		Master's Solution: Dynamic Programming
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		dp = [0] * len(prices) # states info
		minV = prices[0]

		for i in range(1, len(prices)):
			minV = min(minV, prices[i])
			dp[i] = max(dp[i - 1], prices[i] - minV)

		return dp[-1]
# @lc code=end