class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        buffer = deque()
        a = []

        for right_index in range(n):
            left_index = right_index - k
            if buffer and buffer[0] < left_index + 1:
                buffer.popleft()

            while buffer and nums[buffer[-1]] <= nums[right_index]:
                buffer.pop()
            
            buffer.append(right_index)

            if buffer and right_index >= k - 1:
                a.append(nums[buffer[0]])
        return a