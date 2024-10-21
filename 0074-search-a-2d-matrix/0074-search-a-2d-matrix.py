class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #so to search for taret, we can binary search the first of every row.
        #walkthrough:
        #1 < 3, go next 10 > 3, ok 1 is our row. Binary search again on inner row
        # next:
        # 1 < 13, go next, 10 < 13, go next, 23 < 

        #finding row

        row = 0

        top, bot = 0, len(matrix)-1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: #checking ending value, because if 20 > 7, we are too low
                top = row + 1
            elif target < matrix[row][0]: #check now if target is not bigger than ending, check if its less than the first value then we gotta go back up/lower rows
                bot = row - 1
            else:
                #we are in the right place
                break
            
        if not(top <= bot):
            return False
        
        row = (top + bot)//2
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
            