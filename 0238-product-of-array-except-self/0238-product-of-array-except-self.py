class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        ans = [1] * len(nums)
        for i in range(0,len(nums),1):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = postfix[i+1] * nums[i]
                
        for i in range(0,len(ans),1):
            if i == 0:
                ans[i] = 1 * postfix[i+1]
            elif i == len(ans)-1:
                ans[i] = prefix[i-1] * 1
            else:
                ans[i] = prefix[i-1] * postfix[i+1]
        return ans