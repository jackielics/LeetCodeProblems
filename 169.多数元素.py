#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement0(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v > len(nums)//2:
                return k

    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票
        votes = 0
        for v in nums:
            if votes == 0:
                res = v
            votes += 1 if v == res else -1 # 正负票数抵消
        return res
# @lc code=end

