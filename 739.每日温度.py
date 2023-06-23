#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
	def dailyTemperatures0(self, temperatures: List[int]) -> List[int]:
		'''
		My Solution: Brute Force Loop, Time Limit Exceeded 35/48
		Time complexity: O(n^2)
		Space complexity: O(1)
		'''
		res = [] # 1 <= length
		for i in range(len(temperatures)):
			if i == len(temperatures) - 1:
				res.append(0)
				break

			j = i + 1
			while j < len(temperatures):	
				if temperatures[j] > temperatures[i]:
					res.append(j - i)
					break
				j += 1
			if j == len(temperatures):
				res.append(0)

		return res
	
	def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
		'''
		Master's Solution1: Monotonic Decreasing Stack + Pointer
		Time complexity: O(n)
		Space complexity: O(n)
		'''
		res = [0] * len(temperatures)
		monoStack = [] # store index
		for i in range(len(temperatures)):
			curVaule = temperatures[i]
			if not monoStack or curVaule <= temperatures[monoStack[-1]]: # 栈空或者当前值小于等于栈顶值
				monoStack.append(i) # 暂时存储没有得出res的索引
			else: # 栈不空且当前值大于栈顶值
				while curVaule > temperatures[monoStack[-1]]: # 当当前值大于栈顶值时，出栈
					tmp = monoStack.pop()
					res[tmp] = i - tmp
					if not monoStack:
						break
				monoStack.append(i) # 栈空或者当前值小于等于栈顶值，入栈
		# 没被处理的索引，即栈中的索引，对应的res值为0
		return res
	
	def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
		'''
		Master's Solution2: store each temperature's first index(limited)
		Time complexity: O(n)
		Space complexity: O(1)
		'''
		n = len(temperatures)
		# int in [30, 100]
		temp_to_idx = dict() # key: temp, value: index
		res = [0] * n
		inf = 10**9 # Non-existent index 
		# 反向遍历列表，当遍历到 i 时，其右元素都被访问过
		for i in range(n - 1, -1, -1):
			warmer_index = min(temp_to_idx.get(t, inf) for t in range(temperatures[i] + 1, 102))
			if warmer_index != inf: # appeared in temp_to_idx
				res[i] = warmer_index - i
			temp_to_idx[temperatures[i]] = i
		return res
# @lc code=end