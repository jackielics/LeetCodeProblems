#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
	# Refer to: 647. Palindromic Substrings
	def longestPalindrome0(self, s: str) -> str:
		'''Iteration'''
		res = "" # current longest Palindrome

		for mid in range(len(s)): # mid point
			# left and right boundary of Palindrome
			for l, r in ((mid, mid), (mid, mid + 1)): # odd or even length
				while -1 < l <= r < len(s) and s[l] == s[r]:
					if (r - l + 1) > len(res): # new longest
						res = s[l : r + 1] # copy
					l -= 1
					r += 1
		return res

	def longestPalindrome1(self, s: str) -> str:
		'''
        Brute-Force way: depreciated
		'''
		def findPalin(i:int)->dict:
			# i: index, check odd(1) and even(2) meanwhile
			cnt1, cnt2 = 1, 0
			l1, r1 = i - 1, i + 1
			l2, r2 = i, i + 1
			
			# check odd
			while -1 < l1 <= r1 < len(s):
				if s[l1] == s[r1]:
					cnt1 += 2
					l1 -= 1
					r1 += 1
				else:
					break
			
			# check even
			while -1 < l2 <= r2 < len(s):
				if s[l2] == s[r2]:
					cnt2 += 2
					l2 -= 1
					r2 += 1
				else:
					break
			
			if cnt1 >= cnt2: # update
				return {'len':cnt1, 
						'l':l1 + 1, 
						'r':r1 - 1}
			else:
				return {'len':cnt2, 
						'l':l2 + 1, 
						'r':r2 - 1}
		
		ml = l = r = 0
		for i in range(len(s)):
			dic = findPalin(i) 
			if dic['len'] > ml:
				ml = dic['len']
				l, r = dic['l'], dic['r']
		
		return s[l : r + 1]
# @lc code=end