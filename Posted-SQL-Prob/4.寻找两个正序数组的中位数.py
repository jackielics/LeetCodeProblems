#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
	def findMedianSortedArrays0(self, nums1: List[int], nums2: List[int]) -> float:
		'''
		My Solution: merge two sorted arrays and find the median
		Time Complexity: O(m+n)
		Space Complexity: O(m+n)
		'''
		nums1 += nums2 
		nums1.sort()
		med = (nums1[math.floor((len(nums1) - 1)/2)] + nums1[math.ceil((len(nums1) - 1)/2)]) / 2
		return med
	
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		'''
		'''
		total_len = len(nums1) + len(nums2)
		left_len = total_len // 2

		# 判断特殊情况
		import numpy as np
		if (not nums1 or not nums2) or nums1[-1] <= nums2[0]: # nums1在前，nums2在后
			med = np.median(nums1 + nums2)
			return med
		elif nums1[0] >= nums2[-1]: # nums1在后，nums2在前
			med = np.median(nums2 + nums1)
			return med

		l, r = 0, len(nums1) - 1
		m = (l + r) // 2
		while l <= r:
			m2 = left_len - m - 2 # left_len = (m+1)+(m2+1)
			if m2 < 0: # nums2中没有用到的元素
				m = left_len - 1
				break
			if nums1[m] <= nums2[m2 + 1]: # num1满足条件
				if nums2[m2] <= nums1[m + 1]:
					break # 满足条件，划分结束
				else:
					l = m + 1 # 增大m
			else: # num1不满足条件
					r = m - 1 # 减小m
			m = (l + r) // 2 # 下标
			

		# l > r跳出循环的 ,对num1的l、r进行判断
		if r < 0: # nums1未取的
			m2 = left_len - 1
			# m = -1 # 表示不计
		elif l > len(nums1) - 1: # nums1全取的
			m2 = left_len - len(nums1) - 1
		else: # break跳出while循环的
			pass

		# 计算中位数右边的操作数
		if m >= -1 and m2 >= -1:
			right_operand = min(nums1[m + 1], nums2[m2 + 1])
		elif m >= -1:
			right_operand = nums1[m + 1]
		elif m2 >= -1:
			right_operand = nums2[m2 + 1]

		# 计算中位数左边的操作数
		if total_len % 2 == 0:
			if m >= 0 and m2 >= 0:
				left_operand = max(nums1[m], nums2[m2])
			elif m >= 0:
				left_operand = nums1[m]
			elif m2 >= 0:
				left_operand = nums2[m2]
			med = (left_operand + right_operand) / 2
		else:
			med = right_operand

		return med
# @lc code=end