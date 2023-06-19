#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
# Solution1: Time Limit Exceeded
# class Solution:
# 	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
# 		# 可不可以先给arr排序，再给差排序
# 		diff_arr = list(map(lambda y : abs(y - x), arr))
# 		# Selection Sort
# 		for i in range(k):
# 			idx_m = i # index of the minimum
# 			for j in range(i, len(diff_arr)): # find the minimum
# 				if diff_arr[j] < diff_arr[idx_m]:
# 					idx_m = j # update idx_m
# 			# swap
# 			diff_arr[i], diff_arr[idx_m] = diff_arr[idx_m], diff_arr[i]
# 			arr[i], arr[idx_m] = arr[idx_m], arr[i]
# 		return sorted(arr[:k])

# Solution2: Use binary-search
# class Solution:
# 	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
# 		l, r = 0, len(arr)-1 # idx
# 		# Binary Search
# 		while l <= r:
# 			m = (l + r) // 2
# 			if arr[m] == x:
# 				l, r = m , m
# 				break
# 			elif x > arr[m]:
# 				l = m + 1
# 			else:
# 				r = m - 1
# 		# End up with l == r(found) or l == r + 1(404)
# 		if l == r:
# 			lookup = list(range(l - (k-1), l + k)) # lookup range 
# 		else:
# 			lookup =  list(range(l - k, l + k))
# 		# filter out the invalid index
# 		lookup = list(filter(lambda y : y >= 0 and y < len(arr), lookup))
# 		lookup_arr = [arr[i] for i in lookup]

# 		lookup_arr.sort(key=lambda v: abs(v - x))
# 		return sorted(lookup_arr[:k])

# Matser's solution1: stability of sort and sorted function
# class Solution:
#	 def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#		 arr.sort(key=lambda v: abs(v - x))
#		 return sorted(arr[:k])

# Matser's solution2: use bisect_left and window
class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		right = bisect_left(arr, x) # right is the index of the first element >= x
		left = right - 1
		for _ in range(k):
			if left < 0: # left is out of bound, move right till k
				right += 1
			elif right >= len(arr): # right is out of bound, move left
				left -= 1
			elif abs(arr[left] - x) <= abs(arr[right] - x): # left is closer or equal
				left -= 1 # left is smaller, move left
			elif abs(arr[left] - x) > abs(arr[right] - x):
				right += 1
		#  right 可以> len(arr)但是left不能小于0
		return arr[left + 1: right]

# @lc code=end
