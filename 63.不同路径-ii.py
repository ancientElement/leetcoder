#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0: dp[j] = 0 if obstacleGrid[i][j] == 1 else 1
                elif obstacleGrid[i][j] == 1: dp[j] = 0
                else: dp[j] = dp[j] + (dp[j-1] if j > 0 else 0)
        return dp[n-1]
# @lc code=end
# @km code=start
while True:
    try:
        m,n = map(int,input().split())
        obstacleGrid = [list(map(int,input().split())) for _ in range(m)]
        print(Solution().uniquePathsWithObstacles(obstacleGrid))
    except:
        break
# @km code=end
