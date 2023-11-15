class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        srow = 0
        scol = 0
        erow = len(matrix)-1
        ecol = len(matrix[0])-1
        print(f'erow{erow},ecol{ecol}')
        while matrix[srow][scol] < matrix[erow][ecol]:
            if matrix[srow][scol] == target:
                return True
            elif matrix[erow][ecol] == target:
                return True
            if (matrix[srow][scol] < target):
                if (scol+1 > len(matrix[0])-1):
                    srow += 1
                    scol = 0
                else:
                    scol += 1
            if (matrix[erow][ecol] > target):
                if (ecol-1 < 0):
                    erow -= 1
                    ecol = len(matrix[0])-1
                else:
                    ecol -= 1
        if matrix[srow][scol] == target:
            return True
        elif matrix[erow][ecol] == target:
            return True
        return False
        