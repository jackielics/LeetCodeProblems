#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        board1 = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                one = 0
                # 计算0和1的数量
                for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    i1, j1 = i + x, j + y
                    if i1 in range(R) and j1 in range(C):
                        if board[i1][j1] == 1:
                            one += 1
                # 活细胞的情况，否则都死
                if board[i][j] == 1 and one in (2,3) or \
                    board[i][j] == 0 and one == 3:
                    board1[i][j] = 1

        for i in range(R):
            for j in range(C):
                board[i][j] = board1[i][j]


# @lc code=end

