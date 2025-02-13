class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        r_size = gcd(len(str1), len(str2))
        r = str1[0:r_size]

        f1, f2 = len(str1)//r_size, len(str2)//r_size
        if (r * f1) == str1 and (r * f2) == str2:
            return r
        return ""