#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        if n < 3: return n
        dp= [0 for i in range(n+1)]
        dp[0],dp[1],dp[2]=0,1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
# @lc code=end
# @km code=start
def climbStairs(n):
        if n < 3: return n
        dp= [0 for i in range(n+1)]
        dp[0],dp[1],dp[2]=0,1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
while True:
    try:
        n=int(input())
        print(climbStairs(n))
    except:
        break
# @km code=end
