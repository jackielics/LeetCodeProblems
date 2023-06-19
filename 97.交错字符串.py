#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		# s1 for the weight, s2 for the height
		lw, lh = len(s1), len(s2)
		if(lw + lh != len(s3)):
			return False
		# DynamicProgramming list of size (lw + 1) * (lh + 1)
		dp = [[False for _ in range(lw + 1)] for _ in range(lh + 1)]
		dp[0][0] = True # True for begining 
		# range 0, dp[0][.], 
		for i in range(1, lw + 1): # start from 1
			dp[0][i] = (dp[0][i - 1] and s1[i - 1] == s3[i - 1])
		# column 0, dp[.][0]
		for j in range(1, lh + 1):
			dp[j][0] = (dp[j - 1][0] and s2[j - 1] == s3[j - 1])
		
		for i in range(1, lh + 1):
			for j in range(1, lw + 1):
				dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s1[j-1]) \
						or (dp[i-1][j] and s3[i+j-1] == s2[i-1])
		
		return dp[-1][-1]

# Reference:
# https://leetcode.cn/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/
# https://leetcode.cn/problems/interleaving-string/solution/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/

# 大神的代码：较为简洁，不太容易理解
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if(len1+len2!=len3):
            return False
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,len2+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]
# @lc code=end

