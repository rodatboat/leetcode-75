import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size = len(nums)
        mins = [sys.maxsize] * 3

        for n in nums:
            if n < mins[0]:
                mins[0] = n
            if n > mins[0]:
                mins[1] = min(n, mins[1])
            if n > mins[1]:
                return True
        
        return False
        