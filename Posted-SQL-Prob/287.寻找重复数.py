#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
	def findDuplicate0(self, nums: List[int]) -> int:
		'''
		Master's Solution0: Floyd 
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		# 1 <= n
		fast = slow1 = 0
		while not (fast > 0 and fast == slow1):
			slow1 = nums[slow1]
			fast = nums[nums[fast]]
		
		slow2 = 0
		while slow1 != slow2:
			slow1 = nums[slow1]
			slow2 = nums[slow2]

		return slow1
	
	def findDuplicate(self, nums: List[int]) -> int:
		'''
		Master's Solution1: binary-search
		Time Complexity: O(n^2)
		Space Complexity: O(1)
		'''
		# n+1个整数，都在[1,n] 

		# 长度n+1，取值在[1,n] 
		l, r = 1, len(nums) - 1 # 最小值和最大值
		while l < r:
			m = (l + r) // 2 # 往下取整
			cnt = sum([v<=m for v in nums])
			if cnt <= m: # 如果实际值<=理论值，说明重复数在右边(不含)
				l = m + 1 # <=要往右+1,表示当前值不可能重复
			else: # 如果实际值>理论值，说明重复数在左边（含
				r = m # >要往左，当前值也可能是重复的

		return l
# @lc code=end