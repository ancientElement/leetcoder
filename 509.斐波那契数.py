#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        if n == 0: return 0
        dp = [0 for _ in range(n+1)]
        dp[0],dp[1]=0,1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
# @lc code=end
# @km code=start
def fib(n):
        if n == 0: return 0
        dp = [0 for _ in range(n+1)]
        dp[0],dp[1]=0,1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
while True:
    try:
        n = int(input())
        print(fib(n))
    except:
        break
# @km code=end