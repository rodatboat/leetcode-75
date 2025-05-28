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