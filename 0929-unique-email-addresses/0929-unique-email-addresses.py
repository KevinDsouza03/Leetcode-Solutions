class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ans = set()
        
        for i in emails:
            loc_temp = ''
            dom_temp = ''
            local,domain = i.split("@")
            for char in range(0,len(local)):
                if ord(local[char]) == ord("+"):
                    break
                elif ord(local[char]) == ord("."):
                    #skip
                    continue
                else:
                    #add to our temp
                    loc_temp += local[char]
            for char in range(0,len(domain)):
                if ord(domain[char]) == ord("+"):
                    continue
                else:
                    #add to our temp
                    dom_temp += domain[char]
            ans.add(loc_temp + "@" + dom_temp)
        
        
        return len(ans)
                    
                    