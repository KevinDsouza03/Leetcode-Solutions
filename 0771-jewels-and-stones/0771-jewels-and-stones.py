class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        m = {}
        
        for i in jewels:
            m.update({i: 1})
        
        ans = 0
        for i in stones:
            if m.get(i,None) == None:
                continue
            else:
                ans += 1
    
        return ans
            
        