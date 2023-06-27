#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#

# @lc code=start
class TimeMap:
	'''
	My Solution: use {{}} to store {key-{timestamp:value}} and {key-[timestamp]} to store the timestamp list,
		then use binary search to find the target timestamp.
	Time Complexity: O(logn)
	Space Complexity: O(n)
	'''
	def __init__(self):
		self.time_value = dict() # {key:{timestamp:value,...}} 存储键值对
		self.time_list = dict() # {key:[timestamp,...]}存储每个key的timestamp列表

	def set(self, key: str, value: str, timestamp: int) -> None:
		'''
		set 操作中的时间戳 timestamp 都是严格递增的
		'''
		if not self.time_value.get(key, {}): # key doesn't exist
			self.time_value[key] = {} # create a key-{}
		self.time_value[key][timestamp] = value

		if not self.time_list.get(key, {}): # key doesn't exist
			self.time_list[key] = [] # create a key-[]
		self.time_list[key].append(timestamp)


	def get(self, key: str, timestamp: int) -> str:
		'''
		timestamp_prev <= timestamp 。
		返回对应最大的  timestamp_prev 的那个值。
		如果没有值，则返回空字符串（""）。
		'''
		nums = self.time_list.get(key, [])
		if not nums: # key doesn't exist
			return ""
		else:
			# 在对应的key中直接找对应的timestamp
			tmp = self.time_value.get(key, {}).get(timestamp, None)
			if tmp:
				return tmp
		target = timestamp

		l, r = 0, len(nums) - 1
		if target >= nums[-1]: # 大于等于最大的
			return self.time_value[key][nums[-1]]
		elif target < nums[0]: # 小于最小的
			return ""
		

		while l <= r:
			m = (l + r) // 2
			if nums[m] == target:
				return self.time_value[key][nums[m]]
			elif nums[m] > target:
				if m == 0:
					return ""
				elif nums[m - 1] < target:
					return self.time_value[key][nums[m - 1]]
				else:
					r = m - 1
			elif nums[m] < target:
				if m == len(nums) - 1:
					return self.time_value[key][nums[m]]
				elif nums[m + 1] > target:
					return self.time_value[key][nums[m]]
				else:
					l = m + 1



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

