#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		coins.insert(0, 0)

		# DP[AMT][IC]: number of methods sum up to AMT using coins[IC] and not using coins[IC]
		DP = [[0] * len(coins) for _ in range(amount + 1)]
		DP[0] = [1] * len(coins) # special for Zero

		for amt in range(1, len(DP)): # Row：current total amount
			for ic in range(len(coins)): # Col, index of coin: coin being used
				if ic == 0: 
					DP[amt][ic] = 0 
				else: 
					DP[amt][ic] = DP[amt][ic - 1] # inherit 
					if amt >= coins[ic]: # coin can be used
						DP[amt][ic] += DP[amt - coins[ic]][ic] # 

		return DP[-1][-1]
# @lc code=end