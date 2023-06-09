#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0: return False
		if str(x) == str(x)[::-1]:
			return True
		else:	
			return False
	
	# Master's solution: clean and short
	def isPalindrome(self, x: int) -> bool:
		return str(x) == str(x)[::-1]
# @lc code=end

