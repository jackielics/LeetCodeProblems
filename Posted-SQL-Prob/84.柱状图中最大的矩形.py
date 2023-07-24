#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
	def largestRectangleArea0(self, heights: List[int]) -> int:
		'''
		My Solution: Wrong Answer 72/98 cases passed (N/A)
		这种算法虽然不是正确的，但竟然能通过72/98的测试用例
		'''
		res = [] # 每段连续区间的最大高度
		l ,r = 0 ,0 # 1 <= heights.length
		i = 0
		while i < len(heights):
			l = i

			# i是连续区间后的第一个零值点（如果有的话
			while i < len(heights) and heights[i] != 0: 
				i += 1
			tmp = 0
			r = i - 1 # 连续区间的最后一个节点
			
			# 在单个连续区间内寻找最大矩形
			while l <= r:
				tmp = max(tmp, (r - l + 1) * min(heights[l : r+1]))
				if heights[l] <= heights[r]:
					l += 1
				else:
					r -= 1
			res.append(tmp)

			# i是连续零值点后的第一个非零值点
			while i < len(heights) and heights[i] == 0: 
				i += 1
		
		return max(res)
	

	def largestRectangleArea1(self, heights: List[int]) -> int:
		'''
		Master's Solution: Monotonic Stack(increasing)
		'''
		monoStack = [] # [index, heights]
		maxArea = 0

		i = 0
		while i < len(heights):
			if not monoStack or heights[i] >= monoStack[-1][1]: # just add it
				monoStack.append([i, heights[i]])
				i += 1
			# 如果有一片连续相同值，那么只保留首尾
			elif heights[i] == monoStack[-1][1]: #
				if i == len(heights) - 1 or heights[i] != monoStack[-1][1]:
					monoStack.append([i, heights[i]])
				i += 1 # same, skip
			else: # pop all elements less than heights[i]
				pop_list = [] # 本次将要从monoStack中pop出的元素
				while monoStack and monoStack[-1][1] >= heights[i]: # mono非空
					tmp = monoStack.pop()
					pop_list.append(tmp) # 大的在前
					w = pop_list[0][0] - pop_list[-1][0] + 1
					h = min(pop_list[-1][1], pop_list[0][1])
					maxArea = max(maxArea, w * h)
				monoStack.append([tmp[0], heights[i]]) # 往左扩展过的索引

		i = len(monoStack) - 1
		while i >= 0:
			w = monoStack[-1][0] - monoStack[i][0] + 1
			h = min(monoStack[-1][1], monoStack[i][1])
			maxArea = max(maxArea, w * h)
			i -= 1
		
		return maxArea
	
	def largestRectangleArea2(self, heights: List[int]) -> int:
		'''
		Master's Solution: Monotonic Stack but more short and clean, don't use pop_list
		'''
		monoStack = [] # [index, heights]
		maxArea = 0

		for i, h in enumerate(heights): # 简化字母
			flag = False
			while monoStack and h < monoStack[-1][1]:
				im, hm = monoStack.pop()
				maxArea = max(maxArea, hm * (i - im))
				flag = True # 记录pop出的最后一个elem的下标
			
			monoStack.append([im if flag else i, h]) # h>=monoStack[-1][1]时直接入栈
		
		# monoStack里的元素都是可以扩展到末尾的
		for i, h in monoStack:
			maxArea = max(maxArea, h * (len(heights) - i))

		return maxArea
	
	def largestRectangleArea3(self, heights: List[int]) -> int:
		'''
		Master's Solution: avoid boundary conditions by adding 0 to the end of heights
		'''
		stack = [-1] # 避免判断栈空
		area = 0
		heights.append(0) # 避免遍历结束后栈中还有元素，便于heights[stack[-1]]的计算
		for i in range(len(heights)):
			while heights[i] < heights[stack[-1]]:
				h = heights[stack.pop()]
				area = max(area, h * (i - stack[-1] - 1)) # i是右边界，stack[-1]是左边界,-1表示不算 heights[i]
			stack.append(i)
		
		return area
# @lc code=end