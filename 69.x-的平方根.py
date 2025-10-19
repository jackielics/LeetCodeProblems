#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i < x:
            i += 1
        if i*i == x:
            return i
        else:
            return (i - 1)
# @lc code=end