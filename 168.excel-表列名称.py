#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel 表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 无零26进制：注意末位
        res = ''
        while columnNumber:
            columnNumber, rmn = divmod(columnNumber-1, 26)
            res = chr(ord('A') + rmn) + res
                
        return res
# @lc code=end

