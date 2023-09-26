#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
	def longestCommonPrefix0(self, strs: List[str]) -> str:
		res = strs[0] # 1 <= strs.length
		for s in strs[1:]:
			if len(res) > len(s):
				res = res[:len(s)] # conca
			while res and res != s[:len(res)]:
				res = res[:-1] # remove tail
		return res
	
	def longestCommonPrefix1(self, strs: List[str]) -> str:
		'''Asterisk expression'''
		res = ""
		for chars in zip(*strs):
			# same char in same index
			if len(set(chars)) == 1:
				res += chars[0]
			else:
				break
		return res
# @lc code=end

