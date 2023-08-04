#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		'''
		My Solution: updating min speed in Binary Search
		Time Complexity: 	O(N * log(max(piles)))
		Space Complexity:	O(1)
		'''
		if len(piles) == h:
			return max(piles)
		
		l, r = 1, max(piles) # possible speed range
		res = r
		while(l <= r):
			k = (l + r) // 2 # floor
			# ceiling，actual hours
			hours = sum(list(map(lambda x : math.ceil(x / k), piles))) 
			# speed costing h hours is not unique
			if hours <= h:
				res = min(res, k) # update speed
				r = k - 1 # try finding slower speed
			elif hours > h:
				# actual expenditure greater than expected, speed-up needed
				l = k + 1
		return res
	
# Reference: https://www.youtube.com/watch?v=U2SozAs9RzA
# @lc code=end