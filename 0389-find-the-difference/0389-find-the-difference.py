class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s) == 0:
            return t
        
        left = 0
        s = sorted(s)
        t = sorted(t)
        while left < len(s)and left < len(t):
            if t[left] != s[left]:
                return t[left]
            else:
                left += 1
        if left < len(t):
            return t[left]