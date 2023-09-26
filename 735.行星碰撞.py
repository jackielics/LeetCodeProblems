#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
class Solution:
	def asteroidCollision0(self, asteroids: List[int]) -> List[int]:
		# initialize survial/res
		survival = []

		# From left -> right
		# Compare survival[-1] with the upcoming one 
		for cur in asteroids:
			# if empty right now, append directly
			# or same symbol, append directly
			# or <-- survival[-1] &  cur -->
			if not survival or \
				survival[-1] * cur > 0 or \
				survival[-1] < 0 and cur > 0: 
				survival.append(cur)

			# Collide!
			elif survival[-1] > 0 and cur < 0 and abs(survival[-1]) <= abs(cur): # survival[-1] --> & <-- cur
				cur_alive = True
				# Start one round battle until |survival[-1]| < |cur| or <<--survival[-1]
				while survival and survival[-1] > 0:
					# the upcoming destroyed
					# last = survival.pop(-1) # drop the last
					last = survival[-1] # Compare
					if abs(last) == abs(cur):
						cur_alive = False # cur destroyed also
						survival.pop(-1) # drop the last
						break
					elif abs(last) >= abs(cur):
						cur_alive = False # cur destroyed also
						break
					elif abs(last) <= abs(cur):
						survival.pop(-1) # drop the last

				if cur_alive:
					survival.append(cur)

		return survival
	
	def asteroidCollision1(self, asteroids: List[int]) -> List[int]:
		'''More concise: Stack'''
		stack = []
		for cur in asteroids:
			# Only one circumstance of collision
			while stack and cur < 0 and stack[-1] > 0:
				if (diff := cur + stack[-1]) > 0:
					cur = 0 # dont append cur
				elif diff < 0:
					stack.pop() # pop the last
				else:
					cur = 0
					stack.pop()
			if cur: # didn't be set 0
				stack.append(cur)

		return stack
# @lc code=end

