#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		dic = {} # {elem1: next_greater_elem, }
		stack = [] # Monotonic Stack
		for v in nums2:
			# pop all elems smaller than V
			while stack and v > stack[-1]: # not empty, pop out
				pop = stack.pop()
				dic[pop] = v # {elem: next_greater}
			stack.append(v) # push new in

		res = []
		for v in nums1:
			if (nxt := dic.get(v, None)):
				res.append(nxt)
			else:
				res.append(-1)
		
		return res
# @lc code=end