#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#

# @lc code=start
class Solution:
	def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
		'''Return bool can it be a rectangle or not'''
		# list, set and Counter of all coordinates
		cos_all = [(co[0], co[1]) for co in rectangles] + \
					[(co[0], co[3]) for co in rectangles] + \
					[(co[2], co[1]) for co in rectangles] + \
					[(co[2], co[3]) for co in rectangles]
		cos_all_counter = Counter(cos_all) # a dict
		co_set = set(cos_all)
		
		# sum square of all rect literally
		sum_square = sum([(co[2] - co[0]) * (co[3] - co[1]) for co in rectangles])
		
		# Get all boarder points by nexted list comprehension
		xs = sorted([co for cos in rectangles for co in (cos[0], cos[2])])
		ys = sorted([co for cos in rectangles for co in (cos[1], cos[3])])
		left_down = xs[0], ys[0]
		left_up = xs[0], ys[-1]
		right_down = xs[-1], ys[0]
		right_up = xs[-1], ys[-1]
		boarders = {left_down, left_up, right_down, right_up}
		del xs, ys

		# Compare total_square with sum_square
		total_square = (right_up[0] - left_down[0]) * (right_up[1] - left_down[1])
		if total_square != sum_square:
			return False

		# return False if board point doesn't exist
		if not (left_down in co_set and 
				left_up in co_set and
				right_down in co_set and
				right_up in co_set
				):
			return False

		# check overlapping situation for boarder-point and non-boarder-point
		for co in cos_all_counter:
			# boarders but not single
			if co in boarders:
				if cos_all_counter[co] != 1:
					return False
			# not boarders but odd
			elif cos_all_counter[co] % 2 != 0:
					return False

		return True
# @lc code=end