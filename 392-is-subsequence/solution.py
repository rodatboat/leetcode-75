class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len == 0:
            return True
        if t_len < s_len:
            return False
        s_idx = 0
        for t_idx, i in enumerate(t):
            if s_idx < s_len and i == s[s_idx]:
                s_idx += 1
        return s_idx == s_len
        