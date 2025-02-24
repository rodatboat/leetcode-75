class Solution:
    # Solution 1
    def maxOperations(self, nums: List[int], k: int) -> int:
        a = {}
        operations = 0

        for _, i in enumerate(nums):
            e = k - i
            if e in a and a[e] > 0:
                a[e]-=1
                operations+=1
            else:
                if i not in a:
                    a[i] = 0
                a[i] += 1
        return operations
        