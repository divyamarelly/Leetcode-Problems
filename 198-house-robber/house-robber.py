class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2,n+1):
            include = dp[i-2] + nums[i-1]
            exclude = dp[i-1]
            dp[i] = max(include, exclude)
        return dp[n]
