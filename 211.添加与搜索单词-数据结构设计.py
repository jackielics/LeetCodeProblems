#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class Node:
	def __init__(self):
		self.kids = defaultdict(Node) # key-child
		self.end = False # end of word or not

class WordDictionary:
	'''
	Trie Prefix Tree
	'''
	def __init__(self):
		self.root = Node()

	def addWord(self, word: str) -> None:
		cur = self.root
		for i in range(len(word)):
			# defaultdict connect key:value if not exist and move pointer
			cur = cur.kids[word[i]] # move forward
		cur.end = True # an end

	def search(self, word: str) -> bool:
		'''Search with Wildcard.'''
		def dfs(st, cur):
			'''
			st: start index of word
			cur: current node
			'''
			for i in range(st, len(word)):
				# If Wildcard . try every possibilities
				if word[i] == '.':
					for kid in cur.kids.values(): # fetch nodes
						if dfs(i + 1, kid):
							return True
					return False
				elif word[i] not in cur.kids:
					return False
				else:
					cur = cur.kids[word[i]] # move 

			return cur.end # According to the question

		return dfs(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

