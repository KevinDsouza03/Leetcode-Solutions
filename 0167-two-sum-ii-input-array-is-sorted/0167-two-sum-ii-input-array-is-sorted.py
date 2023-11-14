class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1
        while b > a:
            if(target-numbers[a] == numbers[b] or target-numbers[b] == numbers[a]):
                return [a+1,b+1]
            if(numbers[a] < target-numbers[b]):
                a += 1
            elif(numbers[b] > target-numbers[a]):
                b -= 1
        
            
        