#
# @lc app=leetcode.cn id=2463 lang=python3
#
# [2463] 最小移动总距离
#

# @lc code=start
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        factory.sort(key=lambda f: f[0])
        robot.sort()
        m = len(robot)
        f = [0] + [inf] * m
        for pos, limit in factory: # 遍历工厂
            for j in range(m, 0, -1): # 遍历机器人 
                cost = 0 # 从机器人j移动到工厂pos的总距离
                for k in range(1, min(j, limit) + 1): # 遍历机器人j移动的距离
                    cost += abs(robot[j - k] - pos) # 机器人j移动k距离到工厂pos的距离
                    f[j] = min(f[j], f[j - k] + cost) # 机器人j移动k距离到工厂pos的距离 + 机器人j-k移动到工厂pos的最小距离
        return f[m]
    
# @lc code=end

