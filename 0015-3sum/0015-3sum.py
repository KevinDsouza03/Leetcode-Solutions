class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums = sorted(nums)
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
                
            a = i+1
            b = len(nums)-1
            while a < b:
                target = n + nums[a] + nums[b]
                if target > 0:
                    b -= 1
                elif target < 0:
                    a += 1
                else:
                    ans.append([n,nums[a],nums[b]])
                    a += 1
                    while nums[a] == nums[a-1] and a < b:
                        a += 1
        return ans