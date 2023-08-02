#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		'''
		DFS recurse and DP matrix which stores status
		'''
		DP = {} # store status: {(idx, total):cnt of ways}
		def dfs(idx, total):
			if idx == len(nums): # over end
				if total == target: # meet target
					return 1
				else: # miss target
					return 0
			if (idx, total) in DP: # stored before already
				return DP[(idx, total)]
			else:
				DP[(idx, total)] = dfs(idx + 1, total + nums[idx]) \
								+ dfs(idx + 1, total - nums[idx])

			return DP[(idx, total)]

		return dfs(0, 0)

# @lc code=end