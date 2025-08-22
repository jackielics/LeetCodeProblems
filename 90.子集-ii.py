#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())rr
                return

            subset.append(nums[i])
            backtrack(i + 1)

            popped = subset.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return res
# @lc code=end

