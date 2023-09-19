#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
	def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
		'''
		Linear Backtrack
		'''
		if sum(nums) % k != 0:
			return False

		T = sum(nums) // k # Target Value
		if max(nums) > T:
			return False
		
		nums.sort() # ASC
		vst = [False] * len(nums)

		def backtrack(idx, cnt, curSum):
			'''
			i: index considered
			cnt: total filled bucket count
			curSum: sum in current buccntet
			'''
			if cnt == k: # All Buccntets Filled
				return True

			if curSum == T: # Finish Current Buccntet, Start Next Buccntet
				return backtrack(0, cnt + 1, 0)
			
			for i in range(idx, len(nums)):
				# Prune: Skip Duplicates if Tried 
				if i > 0 and not vst[i - 1] and nums[i] == nums[i - 1]:
					continue

				if not vst[i]:
					if curSum + nums[i] <= T:
						vst[i] = True
						if backtrack(i + 1, cnt, curSum + nums[i]):
							return True
						vst[i] = False
					else: # ASC
						break # Jump Out of Loop

			return False # Didn't Worcnt

		return backtrack(0, 0, 0)

	def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
		'''
		Backtrack(147/162): TLE
		'''
		nums.sort(reverse = True)
		if sum(nums) % k != 0:
			return False

		T = sum(nums) // k # Target Value
		if max(nums) > T:
			return False

		global res
		res = False
		def backtrack(i, bucksum):
			'''
			i: Current Index Considered
			buckets: Current Situation
			bucksum: Sum for each bucket
			'''
			if max(bucksum) > T:
				return
			if i >= len(nums):
				if all(x == T for x in bucksum):
					global res
					res = True
				return

			# Consider Where does [i] Go
			for j in range(len(bucksum)): # Id of Bucket
				bucksum[j] += nums[i]
				if bucksum[j] <= T:
					backtrack(i + 1, bucksum)
				bucksum[j] -= nums[i]
		
			return False # Didn't Work

		backtrack(0, [0] * k)
		return res

# @lc code=end