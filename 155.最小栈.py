#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack0:
	'''
	My Solution: use LIST as stack
	'''
	def __init__(self):
		self.lstack = [] # use list as stack, [0] stores the min value

	def push(self, val: int) -> None:
		'''
		将元素val推入堆栈。
		'''
		self.lstack.append(val)
		self.minValue = min(self.lstack)

	def pop(self) -> None:
		'''
		删除堆栈顶部的元素。
		'''
		self.lstack.pop()
		if self.lstack:
			self.minValue = min(self.lstack)


	def top(self) -> int:
		'''
		获取堆栈顶部的元素。
		'''
		return self.lstack[-1]

	def getMin(self) -> int:
		'''
		获取堆栈中的最小元素。
		'''
		return self.minValue

class MinStack1:
	'''
	Master's Solution: use a list to store the min value for each step
	Time complexity: O(1)
	Space complexity: O(n) 
	'''
	def __init__(self):
		self.lstack = [] # use list as stack, [0] stores the min value
		self.minstack = [] # minvalue for each step

	def push(self, val: int) -> None:
		'''
		将元素val推入堆栈。
		'''
		self.lstack.append(val)
		
		self.minstack.append(min(val, self.minstack[-1]) if len(self.lstack) == 1 else val)

	def pop(self) -> None:
		'''
		删除堆栈顶部的元素。
		'''
		self.lstack.pop()
		self.minstack.pop()


	def top(self) -> int:
		'''
		获取堆栈顶部的元素。
		'''
		return self.lstack[-1]

	def getMin(self) -> int:
		'''
		获取堆栈中的最小元素。
		'''
		return self.minstack[-1]
# @lc code=end

