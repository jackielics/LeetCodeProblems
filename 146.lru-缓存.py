#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start

# Definition for doubly-linked list.
class DLNode:
	def __init__(self, key = 0, value = 0):
		self.key, self.value = key, value
		self.next = None
		self.prev = None

class LRUCache:

	def __init__(self, capacity: int):
		'''
		以 正整数 作为容量 capacity 初始化 LRU 缓存
		1 <= capacity
		'''
		self.cap = capacity
		self.len = 0 # initialize length

		self.dic = {} # key-node

		# set dummy node to avoid many edge circumstances
		self.left = DLNode(-1, -1) # left dummy node
		self.right = DLNode(-1, -1) # right dummy node
		self.left.next = self.right # connect
		self.right.prev = self.left
	
	def pop(self)->None:
		'''
		pop the LRU
		'''
		key = self.left.next.key
		self.remove(key)

		return None

	def remove(self, key:int)->int:
		'''
		remove the key and node 
		'''
		node = self.dic[key]
		node.prev.next = node.next
		node.next.prev = node.prev
		self.dic.pop(key)

		self.len -= 1 # change length
		return node.value

	def insert(self, key:int, value:int)->None:
		'''
		insert the key and node in the right
		'''
		node = DLNode(key, value)
		self.dic[key] = node
		# connect
		node.next = self.right
		node.prev = self.right.prev

		self.right.prev.next = node
		self.right.prev = node

		self.len += 1 # change length
		return None


	def get(self, key: int) -> int:
		'''
		如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 
		'''
		if self.dic.get(key, None): # Already existed
			value = self.remove(key)
			self.insert(key, value)
			return value
		else: # Non-exist
			return -1

	def put(self, key: int, value: int) -> None:
		'''
		如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。
		'''
		
		if self.dic.get(key, None): # Already existed: update value
			self.remove(key)
			self.insert(key, value)
		elif self.len < self.cap: # Non-exist and underfilled
			self.insert(key, value)
			pass
			return None
		else: # Non-exist and full(cap>=1)
			self.pop()
			self.insert(key, value)
			pass
			return None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

