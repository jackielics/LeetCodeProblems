#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Node:
	def __init__(self):
		self.kids = {} # key-Node
		self.end = False # can it be an end

class Solution:
	'''
	iterate + DFS
	1 <= m, n <= 12, 1 <= words.length <= 3 * 104
	'''
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		ROWS, COLS = len(board), len(board[0]) # len of rows and cols
		visited = set() # already visited
		res_lst = []

		def build_trie(words):
			# Build a trie from words list
			root = Node() # Root Node
			for word in words:
				cur = root # Current Node
				for c in word:
					if c not in cur.kids:
						# Build if not exist
						cur.kids[c] = Node()
					cur = cur.kids[c] # move next
				cur.end = True # end of a word

			return root # return root Node 


		def dfs(i, j, cur):
			'''
			DFS start from board[i][j]
			i	: row index
			j	: col index
			cur	: current Node
			'''
			if cur == None: # already reach the end
				return True
			
			if (not -1 < i < ROWS or 
       			not -1 < j < COLS or 
				(i, j) in visited or 
				board[i][j] not in cur.kids):
				# repeat || out-of-bound || don't match
				return False
			# if board[i][j] in cur.kids:
			visited.add((i, j)) # add to visited

			# search adjacent to match next char
			# res = (dfs(i + 1, j, tar[1:]) or 
	   		# 		dfs(i, j + 1, tar[1:]) or 
	   		# 		dfs(i - 1, j, tar[1:]) or 
	   		# 		dfs(i, j - 1, tar[1:])
	   		# 		)
			# visited.remove((i, j)) # delete after recursion finished
			if cur.end:
				res_lst.append()
				
			return res
		
		break_flg = False
		for i in range(ROWS):
			for j in range(COLS):
				pass
			# 	if dfs(i, j, word):
			# 		res_lst.append(word)
			# 		break_flg = True
			# 		break
			# if break_flg:break
		
		return res_lst
			
# @lc code=end