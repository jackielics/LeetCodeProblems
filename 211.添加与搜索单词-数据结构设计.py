#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class Node:
	def __init__(self):
		self.kids = {} # key-child
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
			if word[i] not in cur.kids:
				cur.kids[word[i]] = Node()
			cur = cur.kids[word[i]] # move forward
		cur.end = True # an end

	def search(self, word: str) -> bool:
		
		def it_dfs(st, cur):
			'''
			st: start index of word
			cur: current node
			'''
			for i in range(st, len(word)):
				if word[i] == '.': # wildcard
					for v in cur.kids.values(): # fetch nodes
						if it_dfs(i + 1, v):
							return True
					return False

				elif word[i] not in cur.kids:
					return False
				else:	
					cur = cur.kids[word[i]] # move 
		
			return cur.end

		return it_dfs(0, self.root)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

