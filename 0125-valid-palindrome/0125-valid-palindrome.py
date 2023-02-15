import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #modify the string to no spaces and non alphabet
        """
        s = s.lower()
        s = s.replace(" ","") #removes spaces
        #now must remove all non alphabet
        re.sub(r'\W+', '', s) 
        """
        s = ''.join(re.findall(r'[a-zA-Z0-9]', s)).lower()
        start, end = 0, len(s) -1
        print(s)
        while start < end:
            if (s[start] == s[end]):
                start +=1
                end-=1
            else:
                return False
            
        return True