#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows: # 原样返回
            return s

        numZ, remain = divmod(len(s), 2 * numRows - 2) # 有多少个完整Z
        Zcol = numRows - 1
        # 假设 numRows 能凑出一个完整Z
        if remain <= numRows:
            COL = numZ * Zcol + 1
        else:
            COL = numZ * Zcol + 1 + (remain - numRows)
        # 初始化矩阵
        matrix = [[''] * COL for _ in range(numRows)]

        r = c = 0 # 下一个在矩阵中的填充位置
        dir = 1 # 1表示竖直，-1表示斜向
        for i in range(len(s)):
            # 判断：到拐点转向
            matrix[r][c] = s[i]
            # 填充后移动坐标
            if r == numRows - 1: # 拐点
                r -= 1
                c += 1
                dir *= -1 # 转向
            elif r == 0:
                r += 1 # col不变
                if dir == -1:
                    dir *= -1 # 转向
            else: # 非拐点
                if dir == 1:
                    r += 1
                else:
                    r -= 1
                    c += 1

        return ''.join([''.join(x) for x in matrix])
# @lc code=end

