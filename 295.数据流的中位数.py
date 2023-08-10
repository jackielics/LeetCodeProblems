#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
class MedianFinder:

	def __init__(self):
		# self.odd = False # 1,3,5...
		self.q = collections.deque(
				[float('-inf'), 
			      float('-inf'), 
				  float('inf'), 
				  float('inf')])

	def addNum(self, num: int) -> None:
		# [12, 34, 55, 87]
		# 70


	def findMedian(self) -> float:



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

