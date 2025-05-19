class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for idx, val in enumerate(nums):
            solution = target - val # we want the number we need to sum to 'val' to get 'target'
            if solution in s:
                return [s[solution], idx]
            else:
                s[val] = idx

        