class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_tbl = {}
        for i in nums:
            if frequency_tbl.get(i, None) == None:
                frequency_tbl[i] = 1
            else:
                frequency_tbl[i] += 1
        
        items = frequency_tbl.items()
        
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        ans = []
        for key, value in sorted_items:
            ans.append(key)
            if (len(ans) >= k):
                return ans