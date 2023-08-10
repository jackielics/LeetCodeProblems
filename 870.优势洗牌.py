#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
class Solution:
	def advantageCount0(self, nums1: List[int], nums2: List[int]) -> List[int]:
		'''
		TLE
		'''
		nums1.sort() # ASC
		AVL = set(range(len(nums1))) # Available Indexes in NUMS1
		res = []

		for v in nums2: # Base Value in nums2
			FND = False
			for i in AVL: # Find Smallest Greater
				if nums1[i] > v:
					res.append(nums1[i])
					AVL.remove(i) # Unavailable From Now On
					FND = True # Mark Found
					break
			if not FND: # Find Smallest Overall
				i = list(AVL)[0]
				res.append(nums1[i])
				AVL.remove(i)

		return res

	def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
		'''
		Greedy
		'''
		nums1.sort() # ASC
		nums2_idx = sorted(list(enumerate(nums2)), key = lambda x: x[1])
		idx_org, nums2 = [x[0] for x in nums2_idx], [x[1] for x in nums2_idx]

		res_sort = []
		UUD = [] # Unused Index
		# Two-Pointer
		p1 = p2 = 0
		while p1 < len(nums1):
			if nums1[p1] > nums2[p2]: # Exist Greater
				res_sort.append(nums1[p1])
				p1 += 1 # Move Both
				p2 += 1
			else:
				UUD.append(p1)
				p1 += 1 # Move p1 Only
		p1 = 0 # Start from 0
		while p1 < len(UUD):
			res_sort.append(nums1[UUD[p1]])
			p1 += 1

		res = [0] * len(nums2)
		for i in range(len(nums2)):
			res[idx_org[i]] = res_sort[i]

		return res
# @lc code=end