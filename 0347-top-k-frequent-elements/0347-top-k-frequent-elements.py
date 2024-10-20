class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:




        freq_tbl = {}
        for i in nums:
            if freq_tbl.get(i,None) == None:
                freq_tbl[i] = 1
            else:
                freq_tbl[i] = freq_tbl[i] +1


        sort = sorted(freq_tbl.items(), key=lambda x: x[1])
        ans = []
        print(sort)
        i = 0
        while i < k:
            temp = sort.pop()[0]
            ans.append(temp)
            i+=1
        return ans