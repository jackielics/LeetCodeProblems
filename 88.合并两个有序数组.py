#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		# Backwards
		p1, p2 = m - 1, n - 1 # pointer
		# for i in range():
		cur = len(nums1) - 1 # backwards
		while cur >= 0:
			if p2 < 0 or (p1 >= 0 and nums1[p1] >= nums2[p2]):
				nums1[cur] = nums1[p1]
				p1 -= 1 # move p1
			else:
				nums1[cur] = nums2[p2]
				p2 -= 1 # move p2
			cur -= 1
# @lc code=end

