class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a','e','i','o','u']
        r_total = 0
        a = 0  # Initialize a here
        for idx, i in enumerate(s):
            if idx < k:
                if i in v:
                    r_total += 1
                    a += 1
            else:
                if i in v:
                    r_total += 1
                if s[idx-k] in v:
                    r_total -= 1
                if r_total > a:
                    a = r_total
        return a # type: ignore