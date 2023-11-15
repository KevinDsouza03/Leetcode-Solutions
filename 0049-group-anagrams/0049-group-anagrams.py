class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first thought, assigning a value to each char, then calculating.
        #ascii could be a good way, but can get same answer.
        #python should allow for direct comparision though
        #how to store:hashmap? key=calculation, values= arr of anagrams
        #how to run: first try: iterative
        #check each str and if they are found anagram, remove and reevaluate
        
        arr = strs
        ans = {}
        for i in arr:
            str_sort = ''.join(sorted(i))
            if(ans.get(str_sort) == None):
                ans.update({str_sort : []})
                ans[str_sort].append(i)
                continue
            if(ans.get(str_sort) != None):
                ans[str_sort].append(i)
        return(ans.values())
            
            
            
            
            
        
        