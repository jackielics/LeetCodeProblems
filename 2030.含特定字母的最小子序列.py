#
# @lc app=leetcode.cn id=2030 lang=python3
#
# [2030] 含特定字母的最小子序列
#

# @lc code=start
class Solution:
	def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
		# repetition: 还需要重复的次数
		cnt = s.count(letter)
		n = len(s)
		stack = []
		for i, c in enumerate(s):
			while stack and ((c < stack[-1] and len(stack) + n - i > k and (stack[-1] != letter or cnt > repetition)) or k - len(stack) < repetition):
				cur = stack.pop()
				if cur == letter:
					repetition += 1 # 加一

			if len(stack) < k:
				stack.append(c)
				if c == letter:
					repetition -= 1 # 减一

			if c == letter:
				cnt -= 1

		return "".join(stack)

# Reference: https://www.youtube.com/watch?v=IUbWew2HH0s (Mono stack)
# @lc code=end

