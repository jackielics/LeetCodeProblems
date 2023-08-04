#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		if sum(nums) % 2 != 0:
			return False
		else:
			Tar = sum(nums) // 2 # Target Value

		DP = {0} # record all possible sums
		for v in nums:
			st = set() # Temporary Set
			for v1 in DP:
				if v1 + v == Tar: # Find Target
					return True
				st.add(v1 + v)
			DP.update(st) # union 2 Set
		return False
# @lc code=end