#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            if flag == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    flag = 0
        if flag == 1:
            digits = [1] + digits

        return digits
# @lc code=end