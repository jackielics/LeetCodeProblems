#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
	def isValid0(self, s: str) -> bool:
		'''
		My Solution: use LIST as stack
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		if len(s) % 2 == 1:
			return False
		l = []
		for v in s:
			if v in [ '(', '{', '[']:
				l.append(v)
			else:
				if len(l) == 0:
					return False
				if v == ')' and l[-1] == '(':
					l.pop()
				elif v == '}' and l[-1] == '{':
					l.pop()
				elif v == ']' and l[-1] == '[':
					l.pop()
				else:
					return False
		return len(l) == 0
	
	def isValid1(self, s: str) -> bool:
		'''
		Master's Solution: use DICT to store pairs
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		if len(s) % 2 == 1:
			return False
		pairs = {
			'(': ')',
			'[': ']',
			'{': '}'
		}
		l = []
		for v in s:
			if v in list(pairs.keys()):
				l.append(v)
			else:
				if len(l) == 0:
					return False
				elif pairs[l[-1]] == v:
					l.pop()
				else:
					return False
		return len(l) == 0
# @lc code=end