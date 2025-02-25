class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r_total = 0
        a = 0
        for idx, i in enumerate(nums):
            if idx < k:
                r_total += nums[idx]
                a = r_total/k
            else:
                r_total -= nums[idx-k]
                r_total += i
                if r_total/k > a:
                    a = r_total/k
        return a
        