#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000,
                    'IV':4,
                    'IX':9,
                    'XL':40,
                    'XC':90,
                    'CD':400,
                    'CM':900}
        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in mapping:
                res += mapping[s[i:i+2]]
                i += 2
            else:
                res += mapping[s[i]]
                i += 1
        return res
# @lc code=end

