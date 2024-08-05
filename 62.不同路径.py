#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        dp =[1 for _ in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
# @lc code=end
# @km code=start
while True:
    try:
        m,n = map(int,input().split())
        print(Solution().uniquePaths(m,n))
    except:
        break
# @km code=end
