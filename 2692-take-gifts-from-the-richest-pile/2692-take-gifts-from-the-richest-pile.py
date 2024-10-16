class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()

        i = 0
        while i < k:
            temp = int(sqrt(gifts[len(gifts)-1]) // 1)
            gifts[len(gifts)-1] = temp
            gifts.sort()
            i += 1
        
        return sum(gifts)