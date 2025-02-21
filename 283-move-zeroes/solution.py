class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        leftProds = [1] * size
        rightProds = [1] * size

        # Calculate left prods.
        for idx in range(1, size):
            leftProds[idx] = nums[idx-1] * leftProds[idx-1]

        
        # Calculate right prods. size-2, because -1 for correct indexing, and another -1 to avoid index out of bounds for first element.
        for idx in range(size-2, -1, -1):
            rightProds[idx] = nums[idx+1] * rightProds[idx+1]

        for idx, v in enumerate(nums):
            nums[idx] = leftProds[idx] * rightProds[idx]
        
        return nums