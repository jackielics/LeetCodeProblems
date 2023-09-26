#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
class KthLargest:
	'''
	at least k elems guaranteed
	'''
	def __init__(self, k: int, nums: List[int]):
		# only keep k greatest elems
		heap = sorted(nums, reverse = True)[:k] # DSC, drop others
		# min-heap of k elems
		heapq.heapify(heap)
		self.heap = heap
		self.k = k

	def add(self, val: int) -> int:
		# update heap only when val > min(heap)
		if not self.heap:
			self.heap.append(val)
		elif len(self.heap) < self.k:
			heapq.heappush(self.heap, val)
		elif val > self.heap[0]:
			# update heap-top
			heapq.heappop(self.heap)
			# self.heap.pop(0) 
			heapq.heappush(self.heap, val)

		return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

