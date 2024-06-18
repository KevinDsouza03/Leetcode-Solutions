import math
class Solution:
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        if len(piles) == 1:
            temp = piles[0]/h
            return math.ceil(temp)
            
            
        left = 1
        right = max(piles)
        answer = right
        
        while left <= right:
            middle = int((left + right)/2)
            time = 0
            for j in piles:
                time += math.ceil(j / middle)
            if time <= h:
                answer = min(middle, answer)
                right = middle-1
            else:
                left = middle + 1
        return answer