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
		res = ''
		for s in strs:
			res += f'{len(s)}->{s}'
		return res

	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		"""
		cur = 0
		res = []
		while cur < len(s):
			deli = s.index('->', cur) # delimiter start from i
			subLen = int(s[cur : deli])
			cur = deli + 2 + subLen # Update i
			res.append(s[deli + 2 : cur])
		return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

