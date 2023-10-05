#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
	def isValidSudoku0(self, board: List[List[str]]) -> bool:
		'''
		My Solution: Brute-force, 3 loops
		Time Complexity: O(n^2)
		Space Complexity: O(n^2)
		'''
		for i in range(0, 9, 3): # check 3*3
			for j in range(0, 9, 3):
				hash = {}
				for row in board[i : i + 3]:
					for v in row[j : j + 3]:
						hash[v] = hash.get(v, 0) + 1
						if hash[v] > 1 and v != '.':
							return False

		for row in board: # check row
			hash = {}
			for j in row:
				hash[j] = hash.get(j, 0) + 1
				if hash[j] > 1 and j != '.':
					return False
		
		board = list(zip(*board)) # UNPIVOT

		for col in board: # check col
			hash = {}
			for i in col:
				hash[i] = hash.get(i, 0) + 1
				if hash[i] > 1 and i != '.':
					return False
		
		return True
	
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		'''
		Master Solution: [row_index]{num: cnt} with defaultdict()
		Time Complexity: O(n^2)
		Space Complexity: O(n^2)
		'''
		# [row_index]{num: cnt}
		hash_row = [defaultdict(int) for _ in range(9)]
		hash_col = [defaultdict(int) for _ in range(9)]
		hash_box = [defaultdict(int) for _ in range(9)]

		for i in range(9): # check row
			for j in range(9):
				if (v := board[i][j]) != '.': # save time
					hash_row[i][v] += 1
					hash_col[j][v] += 1
					hash_box[(box_id := (i // 3) * 3 + j // 3)][v] += 1

					if any([hash_row[i][v]>1, hash_col[j][v]>1, hash_box[box_id][v]>1]):
						return False

		return True
		
# @lc code=end