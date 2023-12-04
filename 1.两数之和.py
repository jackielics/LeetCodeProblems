#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
	# 1. Brute-Force
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]

	# 2. Hash Dict
	def twoSum1(self, nums: List[int], target: int) -> List[int]:
		hash = {}
		for i in range(len(nums)):
			if target - nums[i] in hash: # will not repeat itself
				return [hash[target - nums[i]], i]
			hash[nums[i]] = i

	# 3. Reverse Hash Dict
	def twoSum2(self, nums: List[int], target: int) -> List[int]:
		hash = {}
		for i in range(len(nums)):
			if nums[i] in hash:
				return [hash[nums[i]], i]
			hash[target - nums[i]] = i
	
	# use `in` and `.index()`
	def twoSum3(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			if target - nums[i] in nums and nums.index(target - nums[i]) != i: # 不是本身
				return [i, nums.index(target - nums[i])]
# @lc code=end

