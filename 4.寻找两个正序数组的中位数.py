#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
	def findMedianSortedArrays0(self, nums1: List[int], nums2: List[int]) -> float:
		'''
		My Solution: brute-force merge two sorted arrays and find the median
		Time Complexity: O((m+n)*log(m+n))
		Space Complexity: O(m+n)
		'''
		nums1 += nums2 
		nums1.sort() # O((m+n)*log(m+n))
		med = (nums1[(len(nums1) - 1)//2] + nums1[len(nums1)//2]) / 2
		return med
	
	def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
		'''
		Left ascending sorted list and Right descending sorted list 
		Time Complexity: O(m+n)
		Space Complexity: O(m+n)
		'''
		# asc(p) & des(q) pointer of nums1 & nums2
		p1 = p2 = 0 
		q1, q2 = len(nums1) - 1, len(nums2) - 1

		total_len =  len(nums1) + len(nums2)
		# Index of left & right operator of median: (n-1)//2, n//2
		left_index, right_index = (total_len - 1) // 2, (total_len) // 2 
		
		if not (nums1 and nums2):
			nums = nums1 + nums2
			return (nums[left_index] + nums[right_index]) / 2
		
		total_asc, total_des = [], []


		while len(total_asc) - 1 < left_index and p1 < len(nums1) and p2 < len(nums2):
			if nums1[p1] <= nums2[p2]: # move the smaller
				total_asc.append(nums1[p1])
				p1 += 1
			else:
				total_asc.append(nums2[p2])
				p2 += 1
		# run out of nums1 before median
		while p1 >= len(nums1) and len(total_asc) - 1 < left_index:
			total_asc.append(nums2[p2])
			p2 += 1 # move p2 & pm meanwhile
		# run out of nums2 before median
		while p2 >= len(nums2) and len(total_asc) - 1 < left_index:
			total_asc.append(nums1[p1])
			p1 += 1 # move p1 & pm meanwhile


		while len(total_des) < total_len - right_index and q1 > -1 and q2 > -1:
			if nums1[q1] >= nums2[q2]: # move the greater
				total_des.append(nums1[q1])
				q1 -= 1
			else:
				total_des.append(nums2[q2])
				q2 -= 1
		# run out of nums1 before median
		while q1 < 0 and len(total_des) < total_len - right_index:
			total_des.append(nums2[q2])
			q2 -= 1 # move p2 & pm meanwhile
		# run out of nums2 before median
		while q2 < 0 and len(total_des) < total_len - right_index:
			total_des.append(nums1[q1])
			q1 -= 1 # move p1 & pm meanwhile

		return (total_asc[-1] + total_des[-1]) / 2
	
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		'''
		binary search in left and right partition
		Time Complexity: O(m+n)
		Space Complexity: O(1)
		'''
		# nums1 cannot be longer than nums2, or (m2 := med - (m1:=(l + r) // 2) - 1) will < 0
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		total_len = len(nums1) + len(nums2)
		med = (total_len - 1) // 2 # Index of (left) median
		# Left Partition: [0, m1] + [0, m2]

		#  Initial pointer for `nums1`
		l, r = 0, len(nums1) - 1

		while True:
			m1 = (l + r) // 2 # current mid in nums1
			# Equation: m1 + 1 + m2 + 1 == med + 1
			m2 = med - m1 - 1 # > 0 because nums1 is shorter
			# Assume -inf is on left of [0], +inf is on right of [-1]
			left1 = nums1[m1] if m1 > -1 else float('-inf')
			right1 = nums1[m1 + 1] if m1 < len(nums1) - 1 else float('inf')

			left2 = nums2[m2] if m2 > -1 else float('-inf')
			right2 = nums2[m2 + 1] if m2 < len(nums2) - 1 else float('inf')

			# partition just right
			if left1 <= right2 and left2 <= right1 :
				if total_len % 2:
					return max(left1, left2)
				else:
					return (max(left1, left2) + min(right1, right2)) / 2
			# Left partition too great -> Decrease Left
			elif left1 > right2:
				r = m1 - 1 
			# Right partition too great -> Increase Left
			else:
				l = m1 + 1
# @lc code=end