class Solution:
    def romanToInt(self, s: str) -> int:
        #thinking using stack, pop top two and do math accordingly
        stack = []
        hashmap = {"I": 1,
                  "V" : 5,
                   "X" : 10,
                   "L" : 50,
                   "C" : 100,
                   "D" : 500,
                   "M" : 1000,
                   "IV" : 4,
                   "IX" : 9,
                   "XL" : 40,
                   "XC" : 90,
                   "CD" : 400,
                   "CM" : 900
                  }
        stack = list(s)
        #input entire thing, then pop 2 at a time and store for math?
        s = 0
        while len(stack) > 0:
            print(s)
            print(stack)
            num1 = stack.pop(0)
            if((num1 == "I" or num1 == "X" or num1 == "C") and len(stack) > 0):
                num2 = stack.pop(0)
                if (hashmap.get(''.join(num1 + num2)) == None):
                    #return newest
                    stack.insert(0,num2)
                    s = s + hashmap[num1]
                    continue
                else:
                    s = s + hashmap[num1+num2]
            else:
                s = s + hashmap[num1]
        return s
            
            
        