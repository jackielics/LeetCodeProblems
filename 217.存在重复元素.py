#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
	'''
	my solution:O(n2), brute-force ,Time Limit Exceeded
	Time:O(n2)
	Space:O(1)
	'''
	def containsDuplicate(self, nums: List[int]) -> bool:
		for i in nums:
			if nums.count(i) > 1:
				return True
			
		return False
	
	'''
	Master's solution1: use set
	Time:O(n)
	Space:O(n)'''
	def containsDuplicate1(self, nums: List[int]) -> bool:
		return len(nums) != len(set(nums))
	
	'''
	Master's solution2:, sort
	Time:O(nlogn)
	Space:O(1)
	'''
	def containsDuplicate2(self, nums: List[int]) -> bool:
		nums.sort()
		for i in range(len(nums) - 1):
			if nums[i] == nums[i+1]:
				return True
		return False
	
	'''
	Master's solution3: use HashSet
	Time:O(n)
	Space:O(n)'''
	def containsDuplicate3(self, nums: List[int]) -> bool:
		hashset = set()
		for n in nums:
			if n in hashset:
				return True
			hashset.add(n)
		return False
# @lc code=end

