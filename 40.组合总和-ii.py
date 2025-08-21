#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		
		res = set()
		curset = [] # current list of elems used
		def backtrack(i, total):
			'''
			i: start index
			total: current total
			'''
			# Bound
			if total == target: # meet target
				res.add(tuple(sorted(curset))) # shallow copy(enough for [int])
				return
			elif total > target or i >= len(candidates):
				return

			curset.append(candidates[i])
			backtrack(i + 1, total + candidates[i]) # try [i]
			curset.pop()
			while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
				i += 1
			backtrack(i + 1, total) # skip [i]

		backtrack(0, 0) # start from i=0, total=0
		
		return [list(x) for x in res]

# @lc code=end