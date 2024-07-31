class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        
        def backtrack(opening,closing, n):
            if opening == closing == n:
                res.append("".join(stack))
                return
            if opening < n:
                stack.append("(")
                backtrack(opening + 1, closing, n)
                stack.pop()
            if closing < opening:
                stack.append(")")
                backtrack(opening, closing + 1, n)
                stack.pop()
        
        backtrack(0,0,n)
        return res
                
        
        
        