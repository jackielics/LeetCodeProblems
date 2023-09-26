#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		neg_stones = [-x for x in stones]
		heapq.heapify(neg_stones)
		# neg_stones
		while neg_stones and len(neg_stones) > 1:
			num1, num2 = heapq.heappop(neg_stones), heapq.heappop(neg_stones)
			if (diff := abs(num1 - num2)): # if Diff != 0, push new elem
				heapq.heappush(neg_stones, -diff)
		if not neg_stones:
			return 0
		else:
			return -neg_stones[0]
# @lc code=end