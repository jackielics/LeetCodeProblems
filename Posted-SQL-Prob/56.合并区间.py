#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		# 先根据区间的左边界排序
		intervals.sort(key=lambda x: x[0])
		res = [intervals[0]] # 1 <= intervals.length

		for l, r in intervals[1:]:
			if l <= res[-1][1]:
				res[-1][1] = max(res[-1][1], r) # merge
			else:
				res.append([l, r]) # just append
		return res
# @lc code=end