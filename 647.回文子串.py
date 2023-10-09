#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
	def countSubstrings0(self, s: str) -> int:
		'''2-DP: T O(n^2) S: O(n^2)'''
		res = 0 # Num of Palindromic Substrings
		# dp[st][ed] == True: [st, ed] is Palindromic
		dp = [[False] * len(s)  for _ in range(len(s))]

		for le in range(1, len(s) + 1): # length-of-substring
			for st in range(len(s)): # start-of-substring
				# end-of-substring
				if (ed := st + le - 1) >= len(s): 
					break # out-of-bound
				if s[st] == s[ed]: # equal on two side
					# if len >= 3 then depend on dp[st + 1][ed - 1]
					dp[st][ed] = dp[st + 1][ed - 1] if le >= 3 else True
					if dp[st][ed]:
						res += 1
		return res
	
	def countSubstrings(self, s: str) -> int:
		'''T O(n^2) S: O(1)'''
		res = 0

		def OutPaliCnt(s, mid, even):
			'''Count of Palindromic Strings from [mid] to outward'''
			l, r = mid, mid + int(even)
			cnt = 0
			# within-boundary and equal
			while -1 < l <= r < len(s) and s[l] == s[r]:
				cnt += 1
				# Outward expansion
				l -= 1
				r += 1
			return cnt
		# Try every start point
		for i in range(len(s)):
			res += OutPaliCnt(s, i, even = False) + OutPaliCnt(s, i, even = True)
		return res
# @lc code=end

