#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Node:
	def __init__(self):
		self.par = None # parent Node
		self.kids = {} # Key-Node
		self.end = False # can it be an end

class Solution:
	'''
	Trie + DFS + Prune
	'''
	def build_trie(self, words):
		'''Build a trie from words list'''
		root = Node() # Root Node
		for word in words:
			cur = root # Current Node
			for c in word:
				if c not in cur.kids:
					# Build if non-existent
					cur.kids[c] = Node()
					cur.kids[c].par = cur
				cur = cur.kids[c] # move next
			cur.end = True # end of a word
		return root # return root Node 
	
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		ROWS, COLS = len(board), len(board[0]) # len of rows and cols
		visited_set = set() # Already visited
		res = []
		# build trie from words
		root = self.build_trie(words)
		
		def prune(cur, chars):
			'''Delete duplicated single path of nodes'''
			# prune node along chars that have only one node?
			for c in chars[::-1]:
				if not cur.kids:
					cur = cur.par # move upward
					cur.kids.pop(c) # delete child
				else:
					break

		def dfs(i, j, cur, chars):
			'''
			DFS start from board[i][j]
			i	: row index
			j	: col index
			cur	: current Node in Trie
			chars: current string
			'''
			# char = board[i][j] # cur char in board
			if (not -1 < i < ROWS or 
				not -1 < j < COLS or 
				(i, j) in visited_set or 
				(char := board[i][j]) not in cur.kids):
				# repeat || out-of-bound || don't match
				return 
			# Add to visited set if board[i][j] in cur.kids:
			visited_set.add((i, j))
			chars += char

			# if reach an end after moving cur 
			if (cur := cur.kids[char]).end:
				res.append(chars) # Return Sentence
				cur.end = False # Avoid Duplicate
				# Delete duplicated single path of nodes
				prune(cur, chars) # faster greatly

			# search adjacent to match next char
			dfs(i + 1, j, cur, chars)
			dfs(i, j + 1, cur, chars)
			dfs(i - 1, j, cur, chars)
			dfs(i, j - 1, cur, chars)
			
			visited_set.remove((i, j)) # delete after recursion finished

		for i in range(ROWS):
			for j in range(COLS):
				dfs(i, j, root, str()) # start from empty string
		
		return res

# @lc code=end