class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        start = 0
        end = -1
        num = list(str(x))
        while (start < len(num)):
            if (num[start] == num[end]):
                start += 1
                end += -1
                print(f"{start} {end}")
                continue
            else:
                return False
        return True
        