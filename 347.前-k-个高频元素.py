#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
	def topKFrequent0(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: use Counter(nums).most_common(k) in Python
		Time Complexity: O(nlogn)
		Space Complexity: O(n)
		'''
		return [i[0] for i in Counter(nums).most_common(k)]

	def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
		'''
		My Solution: use hash and sort
		Time Complexity: O(nlogn)
		Space Complexity: O(n)
		'''
		count = {}
		for i in nums:
			count[i] = count.get(i, 0) + 1
		l = sorted(count.items(), key = lambda x : x[1], reverse = True)
		return [i[0] for i in l[:k]]
		
	def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
		'''
		Master's Solution: use a list which index is frequncy to record frequency and avoid sort
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		count = defaultdict(int) # {key: cnt} default=0
		max_freq = 1
		for i in nums:
			count[i] += 1
			# update `max_freq`
			max_freq = max(count[i], max_freq)

		# All possible frequency [1, max_freq]: freq[index=freq] = key
		freq = [[] for _ in range(max_freq + 1)] # Not * !
		res = []

		for word, cnt in count.items(): # Iter dict
			freq[cnt].append(word)
		for i in range(len(freq) - 1, 0, -1): # backwards
				res += freq[i]
				if k == len(res):
					return res

# @lc code=end