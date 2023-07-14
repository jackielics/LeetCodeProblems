#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		'''
		My Solution 0: DFS Recurse
		'''
		def dfs(cur:int)->int:
			'''
			cur: current change
			Return: min steps of specific value
			'''
			# Recursion Exit
			if cur == 0:
				return 0
			elif cur < 0:
				return float('inf') # inaccessible
			
			# Recursion Body
			if not minSteps.get(cur, None): # non-exist
				mCnt = float('inf')
				# recurse every possibility
				for j in range(len(coins) - 1, -1, -1):
					cnt = dfs(cur - coins[j]) + 1
					# if cnt >= 0:
					mCnt = min(mCnt, cnt) # record
				minSteps[cur] = mCnt

			return minSteps[cur]
		
		minSteps = {} # {value: steps}
		res = dfs(amount)
		return res if res < float('inf') else -1
					
	def coinChange1(self, coins: List[int], amount: int) -> int:
		'''
		Master's Solution: Dynamic Programming
		'''
		# inaccessible [1, amount]
		dp = [float('inf')] * (amount + 1) 
		dp[0] = 0 # initial status, 0 step to access Zero
		for v in range(1, amount + 1):
			for c in coins:
				if v >= c: # update min steps
					dp[v] = min(dp[v], dp[v - c] + 1)
		return dp[-1] if dp[-1] < float('inf') else -1
# @lc code=end