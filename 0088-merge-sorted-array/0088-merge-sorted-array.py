class Solution:
        
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        n1ptr = 0
        n2ptr = 0
        
        while n > 0 and n2ptr < len(nums2) and n1ptr < len(nums1):
                nums1[-n] = nums2[n2ptr]
                n -= 1
                n2ptr += 1
                print(n)
        nums1.sort()
        