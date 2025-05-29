class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])

        max_v = 0
        curr = 0
        n = len(s)
        lptr = 0
        for rptr in range(n):
            if s[rptr] in vowels:
                curr += 1
            if rptr > k-1:
                if s[lptr] in vowels:
                    curr-=1
                lptr += 1

            max_v = max(max_v, curr)
        return max_v