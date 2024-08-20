#
# @lc app=leetcode.cn id=1049 lang=python
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        sum = 0
        for i in range(len(stones)):
            sum = sum + stones[i]
        half = sum // 2
        dp = [0 for _ in range(half+1)]
        for i in range(len(stones)):
            for j in range(half, stones[i]-1, -1):
                dp[j] = max(dp[j],dp[j - stones[i]] + stones[i])
        return sum - dp[half] - dp[half]
# @lc code=end

