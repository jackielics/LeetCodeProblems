#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#

# @lc code=start
class Solution:
	def findLexSmallestString(self, s: str, a: int, b: int) -> str:
		'''list stack recursion'''
		# Define Two Functions
		# Add Operation
		def add(string):
			ret = []
			for i, c in enumerate(string):
				if i % 2:
					ret.append(str((int(c) + a) % 10))
				else:
					ret.append(c)
			return "".join(ret)

		# Rotate Operation using nagetive slice
		rotate = lambda string: string[-b:] + string[:-b]

		res = set()
		stack = [s]
		while stack: 
			cur = stack.pop() # current string
			res.add(cur) # add to res set
			# add and rotate separately
			for val in [add(cur), rotate(cur)]:
				if val not in res:
					stack.append(val)

		return min(res)
# @lc code=end