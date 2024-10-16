class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                #means our target lies in the left -> mid range
                r = mid - 1
            elif nums[mid] < target:
                #mid -> right
                l = mid + 1
            else:
                return mid
        return -1