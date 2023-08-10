#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
	def generateParenthesis0(self, n: int) -> List[str]:
		'''
		My Solution: Brute Force, list each possible combination
		Time Complexity: O(2^(2n)*n)
		Space Complexity: O(n)
		'''
		res = ['('] # 1 <= n
		for i in range(1, 2*n): # 2*n: num of parenthesis
			# Process each string separately
			for j in range(len(res)): 
				if res[j].count('(') == res[j].count(')'): # 只能加(的情况：( == )
					res[j] += '('
				elif res[j].count('(') == n: # 只能加)的情况：( == n
					res[j] += ')'
				else: # 剩余情况都能加
					res.append(res[j]+'(')
					res[j] = res[j]+')'
		return res
	
	def generateParenthesis1(self, n: int) -> List[str]:
		'''
		My Solution: recursion
		Time Complexity: O(4^n/*n)
		Space Complexity: O(n)
		'''
		res = []
		def f(s:str, l:int, r:int): # recursion
			if len(s) == 2*n: # Exit of recursion
				res.append(s)
				return
			if l == r:
				f(s + '(', l + 1, r)
			elif l == n:
				f(s + ')', l, r + 1)
			else:
				f(s + '(', l + 1, r)
				f(s + ')', l, r + 1)
		f('', 0, 0)
		return res
	
# @lc code=end