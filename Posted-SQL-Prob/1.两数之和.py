#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
	# 1. 暴力法
	def twoSum0(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]

	# 2. 哈希表（字典）
	def twoSum1(self, nums: List[int], target: int) -> List[int]:
		hash = {}
		for i in range(len(nums)):
			if target - nums[i] in hash: # 不会重复使用自身
				return [hash[target - nums[i]], i]
			hash[nums[i]] = i

	# 3. 一遍哈希表
	def twoSum2(self, nums: List[int], target: int) -> List[int]:
		hash = {}
		for i in range(len(nums)):
			if nums[i] in hash:
				return [hash[nums[i]], i]
			hash[target - nums[i]] = i
	
	'''用 in xxxlist'''
	def twoSum3(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			if target - nums[i] in nums and nums.index(target - nums[i]) != i: # 不是本身
				return [i, nums.index(target - nums[i])]
# @lc code=end

