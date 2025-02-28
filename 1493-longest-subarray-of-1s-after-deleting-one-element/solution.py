class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        z_total = 0
        r_total = 0
        lidx = 0
        a = 0
        for i in nums:
            if i == 1:
                r_total += 1
            else:
                z_total += 1
            if z_total > 1:
                if nums[lidx] == 1:
                    r_total -= 1
                else:
                    z_total -= 1
                lidx += 1
            if r_total > a:
                if z_total == 0:
                    a = r_total - 1
                else:
                    a = r_total
        return a