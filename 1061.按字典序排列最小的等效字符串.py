#
# @lc app=leetcode.cn id=1061 lang=python3
#
# [1061] 按字典序排列最小的等效字符串
#

# @lc code=start
class Solution:
	def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
		# Alternatives
		alter = [] # [set()]
		p = -1
		while (p := p + 1) < len(s1):
			# Combine intersected
			merged = {s1[p], s2[p]}
			merged_idx = set()
			for i in range(len(alter)):
				# if intersected
				if not alter[i].isdisjoint(merged):
					merged.update(alter[i])
					merged_idx.add(i)
			# remove duplicated and append `merged`
			alter = [alter[i] for i in range(len(alter)) if i not in merged_idx] + [merged]

		# Link char with smallest equivalent in DICT
		equiv = {}
		for s in alter:
			min_eq = min(s)
			for c in s:
				equiv[c] = min_eq

		res = str()
		for c in baseStr:
			res += equiv.get(c, c)

		return res
# @lc code=end