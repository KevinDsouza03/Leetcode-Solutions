class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tbl = {}

        for i,n in enumerate(nums):
            if tbl.get(target-n, None) != None:
                #means we got the answer
                return [tbl.get(target-n),i]
            else:
                tbl[n] = i
 
        return [0,0] 