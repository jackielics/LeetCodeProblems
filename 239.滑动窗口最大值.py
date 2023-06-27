#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
	
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: 不愧是Roadmap的最后一道啊，这么难
		'''
		l = 0
		r = k - 1
		res = []
		for r in range(k - 1, len(nums)):
			l = r - (k - 1)
			res.append(max(nums[l : r + 1]))
		return res



# @lc code=end