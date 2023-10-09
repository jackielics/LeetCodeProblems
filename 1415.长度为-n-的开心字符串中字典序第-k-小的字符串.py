#
# @lc app=leetcode.cn id=1415 lang=python3
#
# [1415] 长度为 n 的开心字符串中字典序第 k 小的字符串
#

# @lc code=start
class Solution:
	def getHappyString0(self, n: int, k: int) -> str:
		ik = k - 1 # let k be index start from 0
		num_body = 2 ** (n - 1) # num of happystrs after prefix
		if ik + 1 > 3 * num_body: # Impossible
			return ""
		
		res = ""
		# Options under specific prefix
		options = {'a': ['b', 'c'], 
					'b': ['a', 'c'], 
					'c': ['a', 'b'], 
					"": ['a', 'b', 'c']
			}
		while num_body > 0:
			pre_idx = ceil((ik + 1) / num_body) - 1 # index of prefix
			res += options.get(res[-1] if res else res)[pre_idx] # res could be ''
			ik %= num_body # new index `k` upder new prefix
			num_body //= 2 # halve num of happystrs upder new prefix

		return res

	def getHappyString1(self, n: int, k: int) -> str:
		'''Brute-Force Recurse'''
		if k > 3 * (2 ** (n - 1)):
			return ''
		# Options under specific prefix
		options = {'a': 'bc', 
					'b': 'ac', 
					'c': 'ab', 
					'': 'abc'
					}
		res = set()
		def recurse(curS):
			# cur: current fixed prefix string
			if len(curS) == n:
				res.add(''.join(curS))
				return
			key = curS[-1] if curS else ''
			for char in options[key]:
				recurse(curS + char)
			return

		recurse(str())
		return sorted(res)[k - 1]
# @lc code=end