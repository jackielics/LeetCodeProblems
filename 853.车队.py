#
# @lc app=leetcode.cn id=853 lang=python3
#
# [853] 车队
#

# @lc code=start
class Solution:
	def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
		'''
		Master's Solution:
		https://www.youtube.com/watch?v=Pr6T-3yB9RM
		Time Complexity: O(nlogn)
		Space Complexity: O(n)
		'''
		pos_time = [(position[i], (target - position[i])/speed[i]) for i in range(len(position))]
		pos_time.sort(key = lambda x: x[0], reverse=True) # Ascending order of position

		res = 0
		i = 0
		while i < len(pos_time):
			res += 1
			j = i + 1
			while j < len(pos_time) and pos_time[i][1] >= pos_time[j][1] : # 起点低，到达终点快
				j += 1
			i = j
		return res

# @lc code=end