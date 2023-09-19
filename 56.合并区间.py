#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		
		# Sort by the left boundary of the interval
		intervals.sort(key=lambda x: x[0])
		res = []

		for l, r in intervals:
			# res not empty & res[-1][0] <= l <= res[-1][1]
			if res and l <= res[-1][1]: 
				res[-1][1] = max(res[-1][1], r) # merge
			else:
				res.append([l, r]) # just append
		return res
# @lc code=end