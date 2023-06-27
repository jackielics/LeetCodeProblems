#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
	def judge_dict(ds:dict, dt:dict)->bool:
		for i in list(dt.keys()):
			if ds.get(i, 0) < dt[i]:
				return False
		return True
	
	def minWindow(self, s: str, t: str) -> str:
		'''
		My Solution0: use DICT to store frequency of each character
		'''
		if len(s) < len(t):
			return ""
		def judge_dict(ds:dict, dt:dict)->bool:
			for i in list(dt.keys()):
				if ds.get(i, 0) < dt[i]:
					return False
			return True
		
		dt, ds = {}, {} # frequency of each character
		l, r = 0, 0 # s中滑动窗口的左右指针
		for i in range(len(t)):
			dt[t[i]] = dt.get(t[i], 0) + 1
		key_list = list(dt.keys()) # 只统计

		while True: # 继续寻找第一个匹配的窗口
			if r >= len(s): # 整个s都无法匹配
				return ""
			if s[r] in key_list:
				ds[s[r]] = ds.get(s[r], 0) + 1
			if judge_dict(ds, dt): # 匹配
				break
			r += 1 # 

		minLen = [r - l + 1, l, r] # len,l,r

		while r < len(s) and l <= r: # 在当前最小窗口的基础上继续找更小的
			if judge_dict(ds, dt): # 当前窗口匹配
				# 尝试更新窗口
				minLen = minLen if minLen[0] <= r - l + 1 else [r - l + 1, l, r]
				if s[l] in key_list:
					ds[s[l]] = ds.get(s[l], 0) - 1
				l += 1 # 从左缩小窗口一格

			elif r < len(s) - 1: # r没到末尾，且当前窗口不匹配
				r += 1
				if s[r] in key_list:
					ds[s[r]] = ds.get(s[r], 0) + 1
			else: # 到末尾了，且当前窗口不匹配
				break
			
		return s[minLen[1] : minLen[2] + 1]


# @lc code=end