class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        d = {} #字典
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        

        for c in t:
            if c not in d:
                return c
            if d[c]<=0:
                return c
            else:
                d[c] = d[c] -1
        return ""
