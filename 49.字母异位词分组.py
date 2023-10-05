#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
	def groupAnagrams0(self, strs: List[str]) -> List[List[str]]:
		'''
		My 	Solution: List and Sort
		5.06 %, 19.14 %
		Time: O(m*nlogn)
		'''
		res = []
		ana_sort = []
		for v in strs:
			if sorted(v) not in ana_sort: # new anagram
				ana_sort.append(sorted(v))
				res.append([v])
			else: # old anagram
				idx = ana_sort.index(sorted(v))
				res[idx].append(v)
		return res

	def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
		'''
		My Solution: use Counter Time Limit Exceeded
		'''
		res = []
		anas = []
		for v in strs:
			ctr = Counter(v)
			if ctr not in anas: # new anagram
				anas.append(ctr)
				res.append([v])
			else:
				idx = anas.index(ctr)
				res[idx].append(v)
		return res
	
	def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
		'''
		Master Solution: defaultdict & HashMap [0] * 26
		'''
		res = defaultdict(list) # collections.defaultdict(list)
		for v in strs:
			cnt = [0] * 26
			for c in v:
				cnt[ord(c) - ord('a')] += 1
			res[tuple(cnt)].append(v) # list cannot be key but tuple can
		return list(res.values())
# @lc code=end

