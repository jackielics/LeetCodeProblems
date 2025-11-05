#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i, v in enumerate(reversed(columnTitle)):
            res += (ord(v) - ord('@')) * (26 ** i)
        return res
# @lc code=end

