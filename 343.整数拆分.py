#
# @lc app=leetcode.cn id=343 lang=python
#
# [343] 整数拆分
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        dp = [0 for i in range(n+1)]
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(1,i):
        
# @lc code=end

