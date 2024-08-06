class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #so we have one that we choose directly, then we sort the rest and do 2 sum sorted
        ans = []
        seen = set()
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0: #means we need to increase left
                    left += 1
                elif nums[i] + nums[right] + nums[left] > 0:
                    right -= 1
                else:
                    ans.append(sorted([nums[i], nums[right],nums[left]]))
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1


        return ans