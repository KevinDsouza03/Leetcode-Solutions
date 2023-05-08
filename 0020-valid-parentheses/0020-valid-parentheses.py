class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {")" : "(", "}" : "{", "]":"["}
        for t in s:
            if (t in characters): #will check if this is clos
                if len(stack) > 0 and stack[-1] == characters[t] : #if open = open
                    stack.pop()
                else:
                    return False
            else:
                stack.append(t)
        if len(stack) == 0:
            return True
        return False
                
        