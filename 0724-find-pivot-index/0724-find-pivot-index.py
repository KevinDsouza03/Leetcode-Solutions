class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        totalSum = sum(nums)

        
        leftSum = 0
        for index,cur in enumerate(nums):
            if leftSum == totalSum-cur-leftSum:
                return index
            else:
                leftSum+= cur
        
    
        return -1