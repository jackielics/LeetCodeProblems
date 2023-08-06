#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
	def threeSum0(self, nums: List[int]) -> List[List[int]]:
		'''
		My Solution: 1.sort 2.two pointers 3.use Set to drop duplicate
		Time Complexity: O(n^2)
		Space Complexity: O(n)
		'''
		nums.sort() # sort asc
		res = set()

		for i in range(len(nums) - 2): # index of elem currently being used
			# Skip duplicates, significantly reduce time
			if i > 0 and nums[i] == nums[i - 1]:
				continue

			tar = -nums[i] # Target sum of two values 
			l, r = i + 1, len(nums) - 1 # don't look back
			while l < r:
				if nums[l] + nums[r] == tar:
					res.add((nums[i], nums[l], nums[r]))
					l += 1
					r -= 1
				elif nums[l] + nums[r] < tar:
					l += 1
				else:
					r -= 1
		
		# transform from {(x,y,z)} to [[x,y,z]]
		res = [list(x) for x in res] 

		return res
	
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		'''
		Master's Solution: skip duplicate in [l] or [r]
		Time Complexity: O(n^2)
		Space Complexity: O(1)
		'''
		nums.sort() # sort asc
		res = []
		
		for i in range(len(nums) - 2): # index of elem currently being used
			# Skip duplicates, significantly reduce time
			if i > 0 and nums[i] == nums[i - 1]: 
				continue

			tar = -nums[i] # Target sum of two values 
			l, r = i + 1, len(nums) -1 # don't look back
			while l < r:
				# skip duplicate in [l] or [r], then no duplicate will be in res
				if l > i + 1 and nums[l] == nums[l - 1]:
					l += 1
					continue
				elif r < len(nums) - 1 and nums[r] == nums[r + 1]:
					r -= 1
					continue

				if nums[l] + nums[r] == tar:
					res.append([nums[i], nums[l], nums[r]])
					l += 1
					r -= 1
				elif nums[l] + nums[r] < tar:
					l += 1
				else:
					r -= 1
		
		return res
# @lc code=end