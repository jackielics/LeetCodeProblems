#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		# Erase the Longest Interval
		intervals.sort()
		st = float('-inf') # Start from -inf
		res = 0

		for l, r in intervals:
			if l >= st: # Non-Overlapping
				st = r # Update 'st' to 'r'
			else: # Overlapping
				res += 1
				st = min(st, r) # Update 'st' to Smaller One

		return res
# @lc code=end