class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row first
        
        hashmap = {}
        for row in board: #selecting rows
            for item in row:
                if item.isnumeric():
                    if hashmap.get(item,None) == None:
                        hashmap.update({item: 1})
                    else:
                        return False
                else:
                    continue
            hashmap.clear()
        #all good on rows, now columns
        
        col = 0
        
        while col < 9:
            for row in board:
                if row[col].isnumeric():
                    if hashmap.get(row[col],None) == None:
                        hashmap.update({row[col]: 1})
                    else:
                        return False
                else:
                    continue
            hashmap.clear()
            col += 1
        
        hashmap.clear()

        
        #now 3x3 boards
        
        x = 0
        y = 0
        iterations = 0
        while iterations < 9:
            for i in range(0,3):
                for j in range(0,3):
                    print(f"y = {y+i}, x = {x+j}")
                    if board[y+i][x+j].isnumeric():
                        if hashmap.get(board[y+i][x+j], None) == None:
                            hashmap.update({board[y+i][x+j]: 1})
                        else:
                            return False
                    else:
                        continue
            hashmap.clear()
            iterations += 1
            if (iterations % 3 == 0):
                x = 0
                y = iterations
                # print(f"y{y}")
            else:
                x = 3 * (iterations%3)
                # print(f"x{x}")
        return True
                
                        
                        
                
                
        
        
        
        