class Solution:
    # DP Top-Down Approach + Memoization
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def helper(i: int):
            if i in memo:
                return memo[i]

            if i == 0:
                memo[i] = nums[0]
                return memo[i]
            if i == 1:
                memo[i] = max(nums[0], nums[1])
                return memo[i]

            memo[i] = max(nums[i] + helper(i-2), helper(i-1))
            return memo[i]

        return helper(n-1)
    
    
    # DP Bottom-Up Approach (aka Tabulation)
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]