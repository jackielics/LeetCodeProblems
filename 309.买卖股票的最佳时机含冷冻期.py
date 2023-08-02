#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		# possible actions
		poss_act = {-2:[-2, 1], 
					# Hold stock and wait: 
					# 1.Keep holding	2.Sell
					-1:[-2, 1], 
					# Buy: 
					# 1.Hold 	2.Sell
					0:[-1, 0], 
					# Coodown with no hold: 
					# 1.Buy 	2.Keep Cooldown
					1:[0], 
					# Sell: 
					# 1.Forced coodown
					}
		DP = {} # {(i_td, act_td, prof_yt): max_total_prof}
		def dfs(i, act_td, prof_yt)->int:
			'''
			i: index of prices(today)
			act: action of TD, -2:hold  -1:buy  0:cooldown  1:sell
			prof_yt: profit as of yesterday
			RETURN: Max Total Profit in given (i, act_td, prof_yt)
			'''
			if i == len(prices): # over bound, transaction ends
				return prof_yt
			# return directly if stored
			if v := DP.get((i, act_td, prof_yt), None):
				return v
			
			# calc profit as of today
			prof_td = prof_yt + (act_td if act_td != -2 else 0) * prices[i]

			# iterate every possible action in tomorrow to calc possible profit
			res = float('-inf')
			for act_tm in poss_act.get(act_td): # possible actions of tomorrow
				res = max(res, dfs(i + 1, act_tm, prof_td))
			DP[(i, act_td, prof_yt)] = res # store status
			
			return res # return max profit
		
		return max(dfs(0, 0, 0), dfs(0, -1, 0)) # starts with COOLDOWN or BUY
# @lc code=end