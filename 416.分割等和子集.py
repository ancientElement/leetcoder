#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        total_sum = 0
        for i in range(len(nums)):
            total_sum = total_sum + nums[i]
        if total_sum % 2 != 0: return False
        half = total_sum // 2
        dp = [0 for _ in range(half+1)]
        for i in range(len(nums)):
            for j in range(half,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
            print(dp)
        return dp[half] == half
# @lc code=end
# @km code=start
while True:
    try:
        num = list(map(int,input().split()))
        print(Solution().canPartition(num))
    except Exception:
        break
# km code=end
