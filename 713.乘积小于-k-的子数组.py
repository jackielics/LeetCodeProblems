#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
	# def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:# sort
	# 	'''两层循环会超时'''
	# 	# 1 <= nums.length 
	# 	# 1 <= nums[i]
	# 	cnt = 0 # return
	# 	p1 = p2 = 0 # two-pointers
	# 	for p1 in range(len(nums)):
	# 		prod = nums[p1]
	# 		for p2 in range(p1, len(nums)):
	# 			# strictly less than k
	# 			if p2 == p1 and nums[p2] < k: # single multiplier
	# 				cnt += 1
	# 			elif p2 > p1:
	# 				prod *= nums[p2]
	# 				if prod < k: # multiple multiplier
	# 					cnt += 1
	# 				else:
	# 					break
	# 	return cnt
	# Master's solution:sliding window
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:# sort
		cnt = 0
		prod = 1
		l = r = 0 # idx
		for r, i in enumerate(nums):
			prod *= i
			while l <= r and prod >= k:
				prod //= nums[l] # must be integer
				l += 1 # move left pointer
			cnt += r - l + 1 #以右端点为结尾的子数组个数
		return cnt
# @lc code=end

