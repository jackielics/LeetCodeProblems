#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotted = []
        fresh = 0
        minute = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotted.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while fresh > 0 and rotted:
            for _ in range(len(rotted)):
                i, j = rotted.pop(0)
                for x, y in directions:
                    i1, j1 = i + x, j + y
                    if i1 in range(ROWS) and j1 in range(COLS) and grid[i1][j1] == 1:
                        grid[i1][j1] = 2
                        rotted.append((i1, j1))
                        fresh -= 1
            minute += 1
        
        return minute if fresh == 0 else -1
# @lc code=end

