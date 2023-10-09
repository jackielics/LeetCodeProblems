#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
	def numDecodings(self, s: str) -> int:
		'''
		My Solution: O(1) 1-DP
		'''
		if s[0] == '0':
			return 0 
		elif len(s) == 1:
			return 1
		# Initialize: pprev, prev [res, last_char]
		pp, p = [1, str()], [1, s[0]]
		for c in s[1:]:
			cur = 0 # current accumulating num of decode 
			# pp to cur: 2 digits s[i-1] + s[i]]
			if 10 <= int(p[1] + c) <= 26: # [10, 26]
				cur += pp[0] # connect 
			# p to cur: 1 digit s[i]
			if 1 <= int(c) <= 9: # [1, 10]
				cur += p[0] # connect 
			# move pointers
			pp = p
			p = [cur, c]

		return cur
# @lc code=end