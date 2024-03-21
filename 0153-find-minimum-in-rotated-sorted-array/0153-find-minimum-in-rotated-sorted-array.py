class Solution:
    def findMin(self, nums: List[int]) -> int:
        #naive way may be to rotate back into sorted, then just check the first. Doubt that is O(log n)
        first_pointer = 0
        last_pointer = len(nums)-1
        minimum = float('inf')
        while (first_pointer < last_pointer):
            print(f"{first_pointer} {last_pointer}")
            if (nums[first_pointer] == 0 or nums[last_pointer] == 0):
                return 0
            minimum = min(minimum,nums[first_pointer])
            minimum = min(minimum,nums[last_pointer])
            first_pointer += 1
            last_pointer -= 1
        print(f"{first_pointer} {last_pointer}")
        minimum = min(minimum,nums[first_pointer])
        if(minimum != float('inf')):
            return minimum
        elif(len(nums) == 1):
            return nums[0]
        else:
            return 0
        