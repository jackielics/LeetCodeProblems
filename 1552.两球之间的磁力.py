#
# @lc app=leetcode.cn id=1552 lang=python3
#
# [1552] 两球之间的磁力
#

# @lc code=start
class Solution:
	def maxDistance(self, pos: List[int], M: int) -> int:
		'''
		Do Bin-SRCH to find the MaxInterval
		'''
		def capacity(INTVL)->int:
			'''
			calc max-capacity in given interval
			'''
			for i in range(len(pos)):
				if i == 0: # first always OK
					res = 1 # return 
					last = pos[i] # last one OK
				else: # not first
					if pos[i] - last >= INTVL: # enough space 
						res += 1
						last = pos[i] # change last

			return res

		pos = sorted(pos)
		if M == 2: # save time
			return pos[-1] - pos[0]
		
		# possible min and max interval in bin-SRCH
		l, r = 1, max(pos) - min(pos)
		res = 1

		while l <= r:
			mid = (l + r) // 2
			
			if capacity(mid) >= M:
				l = mid + 1 # try to increase INTVL
				res = max(res, mid)
			else:
				r = mid - 1 # decrease INTVL

		return res

# @lc code=end