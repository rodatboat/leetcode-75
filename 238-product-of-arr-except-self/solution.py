class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1] * n
        rightProd = [1] * n

        # sum[i:j] = sum[j] - sum[i-1]

        for i in range(1, n):
            leftProd[i] = nums[i-1] * leftProd[i-1]
        
        for i in range(n-2, -1, -1):
            rightProd[i] = nums[i+1] * rightProd[i+1]

        return [leftProd[i] * rightProd[i] for i in range(n)]
        