#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
	def maxProfit0(self, prices: List[int]) -> int:
		'''
		My Solution: just loop but similiar to DP
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		res = 0
		# 1 <= prices.length
		minP = prices[0] # min price so far
		# For each num, find previous less than it
		for price in prices[1:]:
			profit = price - minP
			minP = min(minP, price) # update min Price so far
			res = max(res, profit) # update max profit so far
		return res
	
	def maxProfit1(self, prices: List[int]) -> int:
		'''
		Master's Solution: Dynamic Programming
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		dp = [0] * len(prices) # states info
		minP = prices[0]

		for i in range(1, len(prices)):
			minP = min(minP, prices[i])
			dp[i] = max(dp[i - 1], prices[i] - minP)

		return dp[-1]
# @lc code=end