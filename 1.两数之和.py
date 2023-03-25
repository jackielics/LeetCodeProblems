#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力法
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # 2. 哈希表
        # hash = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in hash:
        #         return [hash[target - nums[i]], i]
        #     hash[nums[i]] = i
        # 3. 一遍哈希表
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]
            hash[target - nums[i]] = i
# @lc code=end

