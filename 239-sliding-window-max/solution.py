class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        a = []
        for idx, i in enumerate(nums):
            # if idx < k - 1:
            while dq and nums[dq[-1]] < i:
                dq.pop()

            dq.append(idx)

            if idx - k == dq[0]:
                dq.popleft()
            
            if idx >= k - 1:
                a.append(nums[dq[0]])
        
        return a