#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
	'''
	iterate + dfs()
	'''
	def exist(self, board: List[List[str]], word: str) -> bool:
		ROWS, COLS = len(board), len(board[0]) # len of rows and cols
		visited = set() # already visited

		def dfs(i, j, tar):
			'''
			DFS start from board[i][j]
			i	: row index
			j	: col index
			tar	: target
			'''
			if tar == '': # already reach the end
				return True
			
			if (not -1 < i < ROWS or 
       			not -1 < j < COLS or 
				tar[0] != board[i][j] or 
				(i, j) in visited):
				return False
			visited.add((i, j)) # add to visited

			# search adjacent to match next char
			res = (dfs(i + 1, j, tar[1:]) or 
	   				dfs(i, j + 1, tar[1:]) or 
	   				dfs(i - 1, j, tar[1:]) or 
	   				dfs(i, j - 1, tar[1:])
	   				)
			visited.remove((i, j)) # delete after recursion finished
			return res

			

		for i in range(ROWS):
			for j in range(COLS):
				if dfs(i, j, word):
					return True
		
		return False

# @lc code=end