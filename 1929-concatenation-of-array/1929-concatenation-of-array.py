class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None]*(len(nums)*2)
        length = len(nums)
        for i in range(0,length*2):
            ans[i] = nums[i % length]
            
        return ans