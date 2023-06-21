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
		nums.sort()
		res = []
		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]: # Significantly reduce time
				continue

			v = -nums[i]
			l, r = i + 1, len(nums) -1
			while l < r:
				if nums[l] + nums[r] == v:
					res.append([nums[i], nums[l], nums[r]])
					l += 1
					r -= 1
				elif nums[l] + nums[r] < v:
					l += 1
				else:
					r -= 1
		
		setRes = set(tuple(i) for i in res)
		# 换回二维list
		res = [list(i) for i in setRes]
		return res
	
	def threeSum1(self, nums: List[int]) -> List[List[int]]:
		'''
		Master's Solution: 遇到重复的数，直接跳过
		Time Complexity: O(n^2)
		Space Complexity: O(1)
		'''
		nums.sort()
		res = []
		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]: # Significantly reduce time
				continue

			v = -nums[i]
			l, r = i + 1, len(nums) -1
			while l < r:
				# skip duplicate
				flag = False
				if l > i + 1 and nums[l] == nums[l-1]:
					l += 1
					flag = True
				if r < len(nums) - 1 and nums[r] == nums[r+1]:
					r -= 1
					flag = True
				if flag:
					continue 

				if nums[l] + nums[r] == v:
					res.append([nums[i], nums[l], nums[r]])
					l += 1
					r -= 1
				elif nums[l] + nums[r] < v:
					l += 1
				else:
					r -= 1
		
		return res
# @lc code=end