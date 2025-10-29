#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(n):
            if n == 1:
                return 1
            return n*factorial(n-1)
        if rowIndex == 0:
            return [1]
        res = []
        for i in range(rowIndex + 1):
            if i in (0, rowIndex):
                res.append(1)
            else:
                res.append(factorial(rowIndex)//(factorial(i)*factorial(rowIndex - i)))
        return res
# @lc code=end

