#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            new = []
            for j in range(i+1):
                if j in (0, i):
                    new.append(1)
                else:
                    new.append(res[i-1][j-1] + res[i-1][j])
            res.append(new)
        return res
# @lc code=end

