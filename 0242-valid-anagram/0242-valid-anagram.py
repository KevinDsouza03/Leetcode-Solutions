class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #want to read through each and do str to int math, and if same it works
        s_sorted = ''.join(sorted(s))
        t_sorted = ''.join(sorted(t))
        if (s_sorted == t_sorted): return True
        return False
        