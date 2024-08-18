class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sTbl = {}
        for idx,char in enumerate(s):
            sTbl.update({char:idx})
        
        tTbl = {}
        for idx,char in enumerate(t):
            tTbl.update({char:idx})
            
        
        tot = 0
        for i in s:
            tot += abs(sTbl.get(i) - tTbl.get(i))
        
        return tot