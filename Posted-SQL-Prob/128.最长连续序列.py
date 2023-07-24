#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
	def longestConsecutive0(self, nums: List[int]) -> int:
		'''
		My Solution: 1. sort 2. traverse
		Time Complexity: O(nlogn)
		Space Complexity: O(1)
		'''
		if not nums:
			return 0
		nums.sort()
		ml = 1 # max length
		cnt = 1
		for i in range(len(nums) - 1):
			if nums[i + 1] - nums[i] == 1:
				cnt += 1
			elif nums[i + 1] - nums[i] == 0:
				continue # stay the same
			else:
				cnt = 1
			if cnt > ml:
				ml = cnt
		return ml
	
	def longestConsecutive1(self, nums: List[int]) -> int:
		'''
		Master's Solution: use Set
		'''
		if not nums:
			return 0
		num_set = set(nums) # remove duplicates
		ml = 1
		for v in num_set:
			# find start of a sequence
			if v-1 not in num_set: 
				p = v # pointer
				cnt = 1
				while p+1 in num_set:
					p += 1
					cnt += 1
				ml = max(ml, cnt)
		return ml

# @lc code=end