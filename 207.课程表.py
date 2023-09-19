#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		graph = {}
		courses = []
		# Build graph
		for c, p in prerequisites:
			graph[c] = graph.get(c, []) + [p] # course: [prequisities]
			courses.append(c)

		vst = set() # visited
		def dfs(cur):
			'''
			cur: current value
			'''
			
			# duplicate, return False directly
			if cur in vst: 
				return False
			# no pre, return True directly
			elif cur not in graph: 
				return True

			else:
				vst.add(cur)
				pres = graph[cur].copy()
				# iterate each pres
				for v in pres: 
					if v in vst: # duplicated
						return False
					elif dfs(v): # removable
						graph[cur].remove(v)

				if graph[cur]:
					return False
				else:
					graph.pop(cur)
					vst.remove(cur)
					return True
		
		# Iterate courses that have pres
		for crs in courses:
			if not dfs(crs):
				return False

		return True

# @lc code=end

