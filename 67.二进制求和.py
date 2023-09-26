#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
	def addBinary0(self, a: str, b: str) -> str:
		return str(bin(int(a, base=2) + int(b, base=2)))[2:]
	
	def addBinary(self, a: str, b: str) -> str:
		ans, car = int(a, 2), int(b, 2)
		# while car != 0
		while car:
			# ans[-1]: ans[-1] + car[-1]
			# car[-2]: carry of `ans[-1] + car[-1]`
			ans, car = ans ^ car, ans & car 
			# After `<< 1`, car[-2]: carry of `ans[-1] + car[-1]`
			car = car << 1

		return bin(ans)[2:]
# @lc code=end

