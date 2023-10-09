#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq

class MedianFinder:

	def __init__(self):
		'''
		Principles:
		len(MinH_Greater) - len(MaxH_Smaller) = {0,1}
		min(MinH_Greater) >= max(MaxH_Smaller)
		'''
		# Separate elems into Min Heap of Greater Elems, Max Heap of Smaller Elems
		self.MinH_Greater, self.MaxH_Smaller = list(), list()

	def addNum(self, num: int) -> None:
		'''adds the num from stream and dynamically resize'''
		if self.MinH_Greater and num > self.MinH_Greater[0]:
			heapq.heappush(self.MinH_Greater, num)
		else:
			heapq.heappush(self.MaxH_Smaller, -num)

		# Exchange Elem to Resize
		if len(self.MinH_Greater) - len(self.MaxH_Smaller) > 1:
			heapq.heappush(self.MaxH_Smaller, -heapq.heappop(self.MinH_Greater))
		elif len(self.MaxH_Smaller) - len(self.MinH_Greater) > 1:
			heapq.heappush(self.MinH_Greater, -heapq.heappop(self.MaxH_Smaller))

	def findMedian(self) -> float:
		'''returns the median of all elements so far'''
		if len(self.MinH_Greater) == len(self.MaxH_Smaller):
			return (self.MinH_Greater[0] - self.MaxH_Smaller[0]) / 2
		elif len(self.MinH_Greater) > len(self.MaxH_Smaller):
			return self.MinH_Greater[0]
		else:
			return -self.MaxH_Smaller[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

