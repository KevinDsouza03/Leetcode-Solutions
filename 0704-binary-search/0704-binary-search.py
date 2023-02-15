class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            if (nums[start] < target):
                start+=1
            if (nums[end] > target):
                end-=1
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1
        