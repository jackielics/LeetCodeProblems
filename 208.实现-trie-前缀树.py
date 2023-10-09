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
	def __init__(self, end = False):
		'''
		ltr: next letter
		'''
		self.next = defaultdict(Node) # next chars {char:Node()}
		self.end = end # end here as a word?

class Trie:
	'''
	Trie Layers: List, Nodes: Dict
	'''
	def __init__(self):
		self.head = Node() # a little space-wasting

	def insert(self, word: str) -> None:
		cur = self.head
		for c in word:
			# defaultdict connect {key:Node()} if no-key
			cur = cur.next[c]
		cur.end = True 

	def search(self, word: str) -> bool:
		cur = self.head
		for c in word:
			if c not in cur.next:
				return False
			cur = cur.next[c]
		return cur.end

	def startsWith(self, prefix: str) -> bool:
		cur = self.head
		for c in prefix:
			if c not in cur.next:
				return False
			cur = cur.next[c]
		return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

