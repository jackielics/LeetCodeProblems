#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
	def maxSlidingWindow0(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: Brute-force, Time Limit Exceeded 37/51 cases passed (N/A)
		'''
		l = 0
		r = k - 1
		res = []
		for r in range(k - 1, len(nums)):
			l = r - (k - 1)
			res.append(max(nums[l : r + 1]))
		return res
	
	def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: use double-end queue as a monotonic decreasing queue
		Time Complexity: O(n)
		Space Complexity: O(k)
		'''
		res = []
		deque = collections.deque() # 双端队列
		l = r = 0

		while r < len(nums):
			while deque and nums[deque[-1]] <= nums[r]:
				deque.pop() # 新元素加入时，从右侧弹出<=新元素的值
			deque.append(r) # 在右侧加入队列
			if r >= k - 1:
				res.append(nums[deque[0]])
				if l == deque[0]: # 最大元素被滑走
					deque.popleft() # 弹出最大元素        
				l += 1
			r += 1
		
		return res
# @lc code=end