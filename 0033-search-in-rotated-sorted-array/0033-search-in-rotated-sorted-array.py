class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            #now check which portion of arr
            
            #left
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid-1
                
                
            else: #right
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
                    
                    
        return -1
        