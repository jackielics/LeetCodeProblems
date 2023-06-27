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
		if len(piles) == h: # 小时数等于堆数
			return max(piles)
		
		l, r = 1, max(piles) # 可能的速度范围
		res = r
		while(l <= r):
			k = (l + r) // 2 # 向下整除
			# 向上取整，实际花费时长
			hours = sum(list(map(lambda x : math.ceil(x / k), piles))) 
			# 花费h小时的速度不唯一
			if hours <= h:
				res = min(res, k) # 更新结果
				r = k - 1 # 尝试找到更小的速度
			elif hours > h:
				# 实际花费大于预计花费，说明速度太慢了，需要加快速度
				l = k + 1
		return res
	

# Reference: https://www.youtube.com/watch?v=U2SozAs9RzA
# @lc code=end