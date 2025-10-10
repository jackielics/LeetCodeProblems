#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray4(self, nums: List[int]) -> List[int]:
        # 4. Select Sort
        for i in range(len(nums) - 1): # [0, len-2]
            for j in range(i + 1, len(nums)): # [1, len-1]
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums

    def sortArray3(self, nums: List[int]) -> List[int]:
        # 3. Bubble Sort
        for i in range(len(nums) - 1, 0, -1): # [1, len-1]
            for j in range(i): # [0, len-2]
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


    def sortArray2(self, nums: List[int]) -> List[int]:
        # 2. Merge Sort
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            left, right = mergesort(arr[:len(arr)//2]), mergesort(arr[len(arr)//2:])

            return merge(left, right)

        def merge(left, right):
            # merge into one
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i < len(left):
                res.extend(left[i:])
            if j < len(right):
                res.extend(right[j:])

            return res

        return mergesort(nums)

    def sortArray1(self, nums: List[int]) -> List[int]:
        # 1. Quick Sort
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left, middle, right = [], [], []
            for x in arr:
                if x < pivot:
                    left.append(x)
                elif x > pivot:
                    right.append(x)
                else:
                    middle.append(x)
            return quicksort(left) + middle + quicksort(right)

        return quicksort(nums)

# @lc code=end

