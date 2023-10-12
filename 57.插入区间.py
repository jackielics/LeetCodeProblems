#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		if not intervals: # 0 <= intervals.length
			return [newInterval]
		# newInterval < intervals
		elif intervals[0][0] > newInterval[1]:
			return [newInterval] + intervals
		# intervals < newInterval
		elif intervals[-1][1] < newInterval[0]:
			return intervals + [newInterval]

		res = []
		for i in range(len(intervals)):
			# Two Non-Overlapping Situations -> directly append new
			if newInterval[0] > intervals[i][1]:
				res.append(intervals[i])
			# Exist `intervals` on the right of `newInterval` -> directly return
			elif newInterval[1] < intervals[i][0]:
				return res + [newInterval] + intervals[i:]
			# Other Complex Overlapping Situations -> update `newInterval`
			else:
				newInterval = [min(newInterval[0], intervals[i][0]), 
								max(newInterval[1], intervals[i][1])]

		# Didn't Close, no interval is on the right of newInterval
		return res + [newInterval]
# @lc code=end