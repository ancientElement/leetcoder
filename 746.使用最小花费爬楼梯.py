#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0 for _ in range(len(cost)+1)]
        dp[0],dp[1] = 0,0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[len(cost)]
# @lc code=end
# @km code=start
def minCostClimbingStairs(cost):
        dp = [0 for _ in range(len(cost)+1)]
        dp[0],dp[1] = 0,0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[len(cost)]
while True:
    try:
        cost = list(map(int,input().split()))
        print(minCostClimbingStairs(cost))
    except:
        break
# @km code=end  
