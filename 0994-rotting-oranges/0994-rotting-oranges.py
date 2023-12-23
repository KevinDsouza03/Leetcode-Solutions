class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotton = 0
        fringe = []
        next_fringe = []
        for i in range(len(grid)):
            # m looping
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if grid[i][j]== 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    rotton += 1
                    next_fringe.append(i)
                    next_fringe.append(j)
        print(f"{fresh}")
        time = 0
        if fresh == 0:
            return 0
        elif rotton == 0:
            return -1
        while len(next_fringe) > 0:
            print("next iter")
            if fresh == 0:
                return time
            time+= 1
            fringe = next_fringe.copy()
            next_fringe.clear()
            while len(fringe) > 0:
                if fresh == 0:
                    return time
                next_row = fringe.pop(0)
                next_col = fringe.pop(0)
                if grid[next_row][next_col] == 2:
                    #add neighbors to fringe. if 1, change to 2 and add their positions to fringe. then continue 
                    try:
                        if grid[abs(next_row-1)][abs(next_col)] == 1:
                            grid[abs(next_row-1)][abs(next_col)] = 2
                            print(f"Putting onto fringe: {abs(next_row-1)}{abs(next_col)}")
                            next_fringe.append(abs(next_row-1))
                            next_fringe.append(abs(next_col))
                            fresh -= 1
                    except:
                        print(f"Out of Range Error at [{next_row-1},{next_col}]")
                        pass
                    try:
                        if grid[abs(next_row+1)][abs(next_col)] == 1:
                            grid[abs(next_row+1)][abs(next_col)] = 2
                            print(f"Putting onto fringe: {abs(next_row+1)}{abs(next_col)}")
                            next_fringe.append(abs(next_row+1))
                            next_fringe.append(abs(next_col))
                            fresh -= 1
                    except:
                        print(f"Out of Range Error at [{next_row+1},{next_col}]")
                        pass
                    try:
                        if grid[abs(next_row)][abs(next_col-1)] == 1:
                            grid[abs(next_row)][abs(next_col-1)] = 2
                            print(f"Putting onto fringe: {abs(next_row)}{abs(next_col-1)}")
                            next_fringe.append(abs(next_row))
                            next_fringe.append(abs(next_col-1))
                            fresh -= 1
                    except:
                        print(f"Out of Range Error at [{next_row},{next_col-1}]")
                        pass
                    try:
                        if grid[abs(next_row)][abs(next_col+1)] == 1:
                            grid[abs(next_row)][abs(next_col+1)] = 2
                            print(f"Putting onto fringe: {abs(next_row)}{abs(next_col+1)}")
                            next_fringe.append(abs(next_row))
                            next_fringe.append(abs(next_col+1))
                            fresh -= 1
                    except:
                        print(f"Out of Range Error at [{next_row},{next_col+1}]")
                        pass
                print(next_fringe)

        if fresh != 0:
            print(f"Ending fresh: {fresh} ")
            return -1
        return time
                