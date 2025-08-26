#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        res = []

        # initial
        preMap = collections.defaultdict(list)
        for x in prerequisites:
            preMap[x[0]].append(x[1])


        def dfs(cur):
            if cur in visited: # repeat
                return False

            visited.add(cur)
            for x in preMap[cur]:
                if not dfs(x):
                    return False
            visited.remove(cur)

            preMap.pop(cur) # already reached
            if cur not in res:
                res.append(cur)
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return []
        return res
# @lc code=end

