#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		# Building Hashmap
		# Time Complexity: O(n)
		n = len(nums)
		hashmap = [0] * (n + 1)
		res = []
		for i in range(n):
			idx = nums[i]
			hashmap[idx] += 1
			if hashmap[nums[i]] == 2:
				res.append(nums[i])
		return res
	
# Master's solution: https://leetcode.cn/problems/find-all-duplicates-in-an-array/solution/shu-zu-zhong-zhong-fu-de-shu-ju-by-leetc-782l/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums) if num - 1 != i]

# @lc code=end