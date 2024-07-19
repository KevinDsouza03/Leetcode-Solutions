class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) < 1:
            return 0
        nums = set(nums)
        
        longest = 0
        
        for n in nums:
            if (n-1) not in nums:
                #start of a seq
                leng = 0
                while n+leng in nums:
                    leng += 1
                longest = max(leng,longest)
            else:
                continue
        
        return longest
        
        
                