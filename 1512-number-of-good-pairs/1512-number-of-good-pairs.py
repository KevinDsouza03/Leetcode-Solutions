class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        
        tbl = {}
        
        for i in nums:
            if tbl.get(i,None) == None:
                tbl.update({i:1})
            else:
                tbl.update({i:tbl.get(i)+1})
        tot = 0
        for i in tbl.values():
            tot += i * (i-1) // 2
        return tot