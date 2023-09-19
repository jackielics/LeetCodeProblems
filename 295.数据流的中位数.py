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
		Rules:
		len(Min_Large) - len(Max_Small) = {0,1}
		min(Min_Large) >= max(Max_Small)
		'''
		# Min Heap of Larger Elems, Max Heap of Smaller Elems
		self.Min_Large, self.Max_Small = [], []

	def addNum(self, num: int) -> None:

		if self.Min_Large and num > self.Min_Large[0]:
			heapq.heappush(self.Min_Large, num)
		else:
			heapq.heappush(self.Max_Small, -num)

		# Exchange Elem to Resize
		if len(self.Min_Large) > len(self.Max_Small) + 1:
			heapq.heappush(self.Max_Small, -heapq.heappop(self.Min_Large))
		elif len(self.Max_Small) > len(self.Min_Large) + 1:
			heapq.heappush(self.Min_Large, -heapq.heappop(self.Max_Small))

	def findMedian(self) -> float:
		if len(self.Min_Large) == len(self.Max_Small):
			return (self.Min_Large[0] - self.Max_Small[0]) / 2
		elif len(self.Min_Large) > len(self.Max_Small):
			return self.Min_Large[0]
		else:
			return -self.Max_Small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

