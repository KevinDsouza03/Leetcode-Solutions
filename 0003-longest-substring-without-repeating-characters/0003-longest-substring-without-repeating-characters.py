class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        current = set()
        
        left = 0
        right = 0
        maxlen = 0
        while right < len(s):
            while s[right] in current:
                current.remove(s[left])
                left += 1
            current.add(s[right])
            maxlen = max(maxlen,len(current))
            right += 1
        return maxlen
            
                
        