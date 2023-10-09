#
# @lc app=leetcode.cn id=2697 lang=python3
#
# [2697] 字典序最小回文串
#

# @lc code=start
class Solution:
	def makeSmallestPalindrome(self, s: str) -> str:
		ls = list(s) # str is immutable
		l, r = -1, len(ls)
		# Double direction
		while (l := l + 1) < (r := r - 1): # Walrus operator
			# Change the larger
			if ord(ls[l]) < ord(ls[r]):
				ls[r] = ls[l]
			if ord(ls[l]) > ord(ls[r]):
				ls[l] = ls[r]

		return ''.join(ls)
# @lc code=end