#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition0(self, s: str) -> List[List[str]]:
        def is_panli(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and is_panli(i + 1, j - 1)

        res = []
        part = []
        def dfs(i: int):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if is_panli(i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

    def partition(self, s: str) -> List[List[str]]:
        '''
        2-DP
        '''
        n = len(s)
        is_panli = [[True] * n for _ in range(n)]

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n): # upper triangle
                is_panli[start][end] = (s[start] == s[end]) and is_panli[start + 1][end - 1]

        res = []
        part = []
        def dfs(i: int):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if is_panli[i][j]:
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

# @lc code=end