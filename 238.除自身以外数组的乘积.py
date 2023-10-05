#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
	def productExceptSelf0(self, nums: List[int]) -> List[int]:
		'''
		My Solution1: Brute Force, 18/22 cases passed
		Time Complexity: O(n^2)
		Space Complexity: O(1)
		'''
		res = []
		for i in range(len(nums)):
			prod = 1
			for j in nums[:i] + nums[i+1:]: # skip nums[i]
				if j == 0:
					prod = 0
					break
				prod *= j
			res.append(prod)
		return res
	
	def productExceptSelf1(self, nums: List[int]) -> List[int]:
		'''
		My Solution2: split
		Time Complexity: O(n)
		Space Complexity: O(n)
		'''
		prod_for = [nums[0]] * len(nums) # 2 <= nums.length
		for i in range(1, len(nums), 1): # forwards
			if prod_for[i - 1] == 0: # all 0 forwards
				prod_for[i:] = [0] * (len(nums) - i)
				break
			prod_for[i] = prod_for[i - 1] * nums[i]

		prod_back = [nums[-1]] * len(nums) # 2 <= nums.length
		for i in range(len(nums) - 2, -1, -1): # backwards
			if prod_back[i + 1] == 0: # all 0 backwards
				prod_back[:i + 1] = [0] * (1 + i)
				break
			prod_back[i] = prod_back[i + 1] * nums[i]

		res = []
		for i in range(len(nums)):
			if i ==0 :
				res.append(prod_back[i + 1])
			elif i == len(nums) - 1:
				res.append(prod_for[i - 1])
			else:
				res.append(prod_for[i - 1] * prod_back[i + 1])

		return res
	
	def productExceptSelf2(self, nums: List[int]) -> List[int]:
		'''
		Master's Solution: don't store prod_for and prod_back
		Time Complexity: O(n)
		Space Complexity: O(1)
		'''
		res = [] # forwards product
		for i in range(len(nums)): # forwards
			if nums[i] == 0: # cur == 0
				res.extend([0] * (len(nums) - i))
				break
			elif not res: # empty
				res.append(nums[i])
			else:
				res.append(res[-1] * nums[i])

		prod = 1 # product from backwards
		for i in range(len(nums) - 1, -1, -1): # [1, len(nums) - 1, -1]
			if prod == 0: # cur == 0
				res[:i + 1] = [0] * (i + 1)
				break
			elif i == 0: # at head
				prod *= nums[i + 1]
				res[i] = prod
			elif i == len(nums) - 1: # at tail
				res[i] = res[i - 1]
			else:
				prod *= nums[i + 1]
				# res[i] = res[i + 1] * nums[i + 1]
				res[i] = prod * res[i - 1]

		return res
# @lc code=end