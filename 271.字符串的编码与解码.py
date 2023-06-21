#
# @lc app=leetcode.cn id=271 lang=python3
#
# [271] 字符串的编码与解码
#

# @lc code=start
class Codec:
	'''
	My Solution: use join and split in Python, and '，'
	'''
	def encode(self, strs: List[str]) -> str:
		"""Encodes a list of strings to a single string.
		"""
		return '，'.join(strs)
		

	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		"""
		return s.split('，')


class Codec1:
	'''
	Master's Solution1: use Delimiter, more general way
	'''
	def encode(self, strs: List[str]) -> str:
		"""Encodes a list of strings to a single string.
		"""	
		if strs == []:
			return "0->"
		res = ''
		for s in strs:
			res += str(len(s))+'->'+s
		return res

	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		"""
		if s == "0->":
			return ['']
		i = 0
		res = []
		while i < len(s):
			deli = s.index('->', i)
			subLen = int(s[i : deli])
			i = deli+2+subLen
			res.append(s[deli+2 : i])
		return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

