class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #so to search for taret, we can binary search the first of every row.
        #walkthrough:
        #1 < 3, go next 10 > 3, ok 1 is our row. Binary search again on inner row
        # next:
        # 1 < 13, go next, 10 < 13, go next, 23 < 

        #finding row

        row = 0

        
        for i in range(0,len(matrix)):
            if matrix[i][0] == target or matrix[i][len(matrix[i])-1] == target:
                return True
            if matrix[i][0] < target and matrix[i][len(matrix[i])-1] > target:
                row = i
                break
        
        l, r = 0, len(matrix[row])-1

        while l <= r:
            mid = l + (r-l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            