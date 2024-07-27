class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftEdges = {}
        rightEdges = {}
        
        
        temp = 0
        for index,num in enumerate(nums):
            leftEdges.update({index:temp})
            temp+= num
        
        temp = 0
        for i in range(len(nums)-1,-1,-1):
            rightEdges.update({i:temp})
            temp+= nums[i]
        
        print(leftEdges)
        print(rightEdges)
        
        for i in leftEdges.keys():
            if leftEdges[i] == rightEdges[i]:
                return i
        
        
        return -1