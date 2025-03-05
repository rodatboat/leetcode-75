class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        s = {}
        for i in arr:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1

        a = {}
        for i in s.values():
            a[i] = True
        
        return len(s.keys()) == len(a.keys())