class Solution:
    def maxArea(self, height: List[int]) -> int:
        #so, we want to find the largest on left side, then the second largest on the right while also maximizing length/distance.
        start = 0
        end = len(height)-1
        maximum = 0
        flip = True
        while(end > start):
            if (min(height[end],height[start]) * (end-start) > maximum):
                print(f"Curr Max{maximum} , we are at start{start} end{end}")
                maximum = min(height[end],height[start]) * (end-start)
                print(f"New max{maximum} ")
                continue
            else:
                if (height[end] > height[start]):
                    start += 1
                    flip = False
                else:
                    end -= 1
                    flip = True
        return maximum
        