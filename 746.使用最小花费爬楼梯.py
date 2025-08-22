#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(dp)):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
            
        return dp[-1]
# @lc code=end

