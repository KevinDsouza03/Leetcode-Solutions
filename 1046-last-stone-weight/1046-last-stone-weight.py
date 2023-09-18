class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #input everything into heap. pop top two, do math, input back. continue till 1
        h = []
        for i in stones:
            heapq.heappush(h,i * -1)
        print(h)
        while len(h) > 1:
            top1 = abs(heapq.heappop(h))
            top2 = abs(heapq.heappop(h))
            heapq.heappush(h, (top1-top2) * -1)
            print(h) 
        return (abs(heapq.heappop(h)))
            
        