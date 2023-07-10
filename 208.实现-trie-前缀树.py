#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

class Node:
	'''
	Node of Trie
	'''
	def __init__(self, isEnd = False):
		'''
		ltr: next letter
		'''
		self.next = {}
		self.isEnd = isEnd

class Trie:
	'''
	My Solution 0: Layers: List, Nodes: Dict
	'''
	def __init__(self):
		self.head = Node() # a little space-wasting

	def insert(self, word: str) -> None:
		cur = self.head

		for v in word:
			if v not in cur.next:
				cur.next[v] = Node()
			cur = cur.next[v]
		cur.isEnd = True
	
	def search(self, word: str) -> bool:
		cur = self.head
		for v in word:
			if v not in cur.next:
				return False
			cur = cur.next[v]
		return cur.isEnd

	def startsWith(self, prefix: str) -> bool:
		cur = self.head
		for v in prefix:
			if v not in cur.next:
				return False
			cur = cur.next[v]
		return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

