class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #so we have a 1 row, n col. bot to top initalized w 1
        
        for i in range(m - 1): #basically, you're going row - 1 since we know the last row's col val is always 1
            newRow = [1] * n #above row/temp row
            for j in range (n - 2,-1,-1): # -2 means we are second to last since last is 1. and going down until -1
                newRow[j] = newRow[j+1] + row[j] #so, we have our row initalized to 1 which represents the number of moves to get 
                #closer to the bottom right. so, we need to take into account the right move's TOTAL and the BOTTOM TOTAL
                #this is done then by j+1 and the row below us. Finally, this is input into the new array and copied 
                #from one to another so we have a bottom row. at end, we simply return our first index as this is the 
                #top left corner.
            row = newRow
        return row[0]