#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
	def combinationSum0(self, candidates: List[int], target: int) -> List[List[int]]:
		if min(candidates) > target:
			return []

		res = []
		def backtrack(tar, st, cur):
			'''
			tar:	target value
			i: 		start index being used
			cur: 	current used elems
			'''
			if (v := tar - candidates[st]) < 0:
				return None
			elif v == 0: # exactly meet target
				res.append(cur + [candidates[st]])
				return None
			else: 
				for i in range(st, len(candidates)): # move forward
					backtrack(v, i, cur + [candidates[st]])

		for i in range(len(candidates)):
			backtrack(target, i, [])

		return res
	
	def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
		if min(candidates) > target:
			return []
		
		res = []
		def backtrack(i, cur, total):
			'''
			i: start index
			cur: current list of elems used
			total: current total
			'''
			# Bound
			if total == target: # meet target
				res.append(cur.copy()) # shallow copy(enough for [int])
				return
			elif total > target or i >= len(candidates):
				return

			cur.append(candidates[i])
			backtrack(i, cur, total + candidates[i]) # try [i]
			cur.pop()
			backtrack(i + 1, cur, total) # skip [i]

		backtrack(0, [], 0) # start from i=0, cur=[], total=0
		
		return res
# @lc code=end