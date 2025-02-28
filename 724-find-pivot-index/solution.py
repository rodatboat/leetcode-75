class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        ridx = len(nums) - 1
        sum_l = []
        sum_r = []
        for idx, i in enumerate(nums):
            if idx == 0:
                sum_l.append(i)
                sum_r.append(nums[ridx])
            else:
                sum_l.append(sum_l[idx-1] + i)
                sum_r.insert(0, sum_r[0] + nums[ridx])
            ridx -= 1

        for i in range(len(nums)):
            if sum_l[i] == sum_r[i]:
                return i
        return -1