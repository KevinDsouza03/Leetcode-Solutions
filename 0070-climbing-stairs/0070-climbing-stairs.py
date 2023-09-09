class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        arr = [0] * (n+4)
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2
        arr[3] = 3
        
        for i in range(4, n + 1):
            arr[i] = arr[i - 1] + arr[i-2]
        
        return arr[n]
