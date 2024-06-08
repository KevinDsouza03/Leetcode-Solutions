class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        #make the min-heap
        self.k = k
        self.heap = sorted(nums,reverse=True)

    def add(self, val: int) -> int:
        #insert into heap, return original k?
        self.heap.append(val)
        self.heap = sorted(self.heap, reverse=True)
        while (len(self.heap) != self.k):
            self.heap.pop()
        return self.heap[-1]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)