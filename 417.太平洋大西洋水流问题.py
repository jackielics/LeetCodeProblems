#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		ADJ = ((-1, 0), (1, 0), (0, -1), (0, 1)) # Up Down Left Right
		R, C = len(heights), len(heights[0])

		po_shore = {(0, x) for x in range(len(heights[0]))} | {(x, 0) for x in range(1, len(heights))}
		ao_shore = {(x, C - 1) for x in range(len(heights))} | {(R - 1, x) for x in range(len(heights[0]))}

		# From Seaside to land
		po_vst = set()
		shore = list(po_shore)
		for item in shore:
			i, j = item[0], item[1]
			bfs = [(i, j)] # BFS Que, Starting Point
			if (i, j) not in po_vst:
				while bfs:
					i, j = bfs.pop(0) # Pop First
					po_vst.add((i, j)) # Mark Visited
					for off in ADJ:
						hi, hj = i + off[0], j + off[1]
						# Within-Bounds & Not Visited Before
						if 0 <= hi < R and 0 <= hj < C and\
							(hi, hj) not in po_vst and heights[hi][hj] >= heights[i][j]:
							po_vst.add((hi, hj))
							bfs.append((hi, hj))
		# po_vst
		ao_vst = set()
		shore = list(ao_shore)
		for item in shore:
			i, j = item[0], item[1]
			bfs = [(i, j)] # BFS Que, Starting Point
			if (i, j) not in ao_vst:
				while bfs:
					i, j = bfs.pop(0) # Pop First
					ao_vst.add((i, j)) # Mark Visited
					for off in ADJ:
						hi, hj = i + off[0], j + off[1]
						# Within-Bounds & Not Visited Before
						if 0 <= hi < R and 0 <= hj < C and\
							(hi, hj) not in ao_vst and heights[hi][hj] >= heights[i][j]:
							ao_vst.add((hi, hj))
							bfs.append((hi, hj))

		return [list(x) for x in ao_vst.intersection(po_vst)]
# @lc code=end

