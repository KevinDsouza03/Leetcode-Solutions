class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        
        stack = []
        
        for count,ele in enumerate(temperatures):
            if count == 0:
                stack.append([ele, count])
                continue
            while len(stack) > 0 and ele > stack[-1][0]:
                poppedEle = stack.pop()
                ans[poppedEle[1]] = count - poppedEle[1]
            stack.append([ele, count])
        return ans
            