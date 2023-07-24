#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
	def numDecodings(self, s: str) -> int:
		'''
		My Solution: 1-DP
		Sketch Illustration: https://www.figma.com/file/nKepYBkoPhAFDj0czjRgur/Untitled?type=whiteboard&node-id=0-1&t=MZ38tUmibY1ycYYW-0
		'''
		if s[0] == '0':
			return 0 
		elif len(s) == 1:
			return 1
		
		# Initialize: pprev, prev [res, last_char]
		pp, p = [1, '1'], [1, s[0]] 
		for c in s[1:]:
			cur = 0
			# pp to cur [s[i-1], s[i]]
			if 10 <= int(p[1]+c) <= 26: # [10, 26]
				cur += pp[0] # connect 
			# p to cur s[i]
			if 1 <= int(c) <= 9: # [1, 10]
				cur += p[0] # connect 
			# move pointers
			pp = p
			p = [cur, c]

		return p[0]
# @lc code=end