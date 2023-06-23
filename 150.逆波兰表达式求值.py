#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		operators = ['+', '-', '*', '/']
		calcStack = []
		for s in tokens:
			if s not in operators:
				calcStack.append(s)
			else:
				r = calcStack.pop()
				l = calcStack.pop()
				exp = l + s + r
				calcStack.append(str(int(eval(exp))))
		
		return int(calcStack[0])
# @lc code=end