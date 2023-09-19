#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
	def fourSum0(self, nums: List[int], target: int) -> List[List[int]]:
		'''
		Specific Method for 4Sum
		'''
		nums.sort() # sort asc
		res = []

		# Each of the four elements is different
		for i in range(len(nums) - 3): # index of elem currently being used
			# Skip Duplicates
			if i > 0 and nums[i] == nums[i - 1]: 
				continue

			for j in range(i + 1, len(nums) - 2): # index of elem currently being used
				# Skip Duplicates
				if j > i + 1 and nums[j] == nums[j - 1]: 
					continue

				tgt = target - nums[i] - nums[j] # Target Sum of Two Values 
				l, r = j + 1, len(nums) -1 # don't look back
				while l < r:
					# skip duplicate in [l] or [r], then no duplicate will be in res
					while l < r and l > j + 1 and nums[l] == nums[l - 1]:
						l += 1
					while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
						r -= 1
					
					# Bounds Checker
					if l >= r:
						break
					elif nums[l] + nums[r] == tgt:
						# if nums[l] != nums[r]: # Different
						res.append([nums[i], nums[j], nums[l], nums[r]])
						l += 1
						r -= 1
					elif nums[l] + nums[r] < tgt:
						l += 1
					else:
						r -= 1
		
		return res
	
	def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
		'''
		Generic Method for NSum
		'''
		nums.sort() # sort asc
		res = []

		def NSum(N, st, tgt, cur):
			'''
			N: Amount of Elems
			st:	Starting index
			tgt: Target Value
			cur: Current list[]
			'''
			if N >= 3:
				for i in range(st, len(nums) - N + 1): # index of elem currently being used
					# Skip Duplicates
					if i > st and nums[i] == nums[i - 1]: 
						continue
					else:
						NSum(N = N - 1, st = i + 1, tgt = tgt - nums[i], cur = cur + [nums[i]])

			else: # <= 2
				l, r = st, len(nums) -1 # don't look back
				while l < r:
					# skip duplicate in [l] or [r], then no duplicate will be in res
					while l < r and l > st and nums[l] == nums[l - 1]:
						l += 1
					while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
						r -= 1

					# Bounds Checker
					if l >= r:
						break
					elif nums[l] + nums[r] == tgt:
						# if nums[l] != nums[r]: # Different
						res.append(cur + [nums[l], nums[r]])
						l += 1
						r -= 1
					elif nums[l] + nums[r] < tgt:
						l += 1
					else:
						r -= 1

		NSum(4, 0, target, [])
		return res
# @lc code=end

