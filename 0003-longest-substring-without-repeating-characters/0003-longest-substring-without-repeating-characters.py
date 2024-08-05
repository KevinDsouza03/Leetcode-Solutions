class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        current = {}
        
        left = 0
        right = 1
        
        maxlen = 1
        temp = 1
        current.update({s[left]: 0})
        while right < len(s):
            if current.get(s[right],None) == None: # good
                current.update({s[right]:right})
                temp += 1
                right += 1
            else: #not good
                maxlen = max(maxlen,temp)
                temp = 1
                left = current.get(s[right]) + 1
                right = left + 1
                current.clear()
                current.update({s[left]: left})
        maxlen = max(maxlen,temp)
        return maxlen
            
                
        