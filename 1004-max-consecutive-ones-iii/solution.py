class Solution:
    def replaceZeros(self, k: int, z_total: int) -> int:
        if z_total <= k:
            return z_total
        else:
            return k

    def longestOnes(self, nums: List[int], k: int) -> int:
        r_total = 0
        z_total = 0
        a = 0
        lidx = 0
        for idx, i in enumerate(nums):
            if i == 1:
                r_total += 1
            else:
                z_total += 1
                
            if z_total > k:
                if nums[lidx] == 1:
                    r_total -= 1
                else:
                    z_total -= 1
                lidx += 1
            if (r_total + self.replaceZeros(k, z_total)) > a:
                a = r_total + self.replaceZeros(k, z_total)
        return a
