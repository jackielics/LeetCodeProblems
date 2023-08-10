#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
	def topKFrequent0(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: use Counter in Python
		Time Complexity: O(nlogn)
		Space Complexity: O(n)
		'''
		return [i[0] for i in Counter(nums).most_common(k)]

	def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: use hash
		Time Complexity: O(nlogn)
		Space Complexity: O(n)
		'''
		count = {}
		for i in nums:
			count[i] = count.get(i, 0) + 1
		l = sorted(count.items(), key = lambda x : x[1], reverse = True)
		return [i[0] for i in l[:k]]
		
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		'''
		Master's Solution: use LIST to store the frequency and avoid sorting
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		count = {}
		freq = [[] for _ in range(len(nums) + 1)] # [] * n is wrong
		res = []
		for i in nums:
			count[i] = count.get(i, 0) + 1
		for key, value in count.items():
			freq[value].append(key)
		for i in range(len(freq) - 1, 0, -1): # backwards
				res += freq[i]
				if k == len(res):
					return res

# @lc code=end