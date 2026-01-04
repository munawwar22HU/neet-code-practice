class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for row in range(9):
            rowMap = set()
            for col in range(9):
                value = board[row][col]
                if value != ".":
                    if value not in rowMap:
                        rowMap.add(value)
                    else:
                        return False
                
        for col in range(9):
            colMap = set()
            for row in range(9):
                value = board[row][col]
                if value != ".":
                    if value not in colMap:
                        colMap.add(value)
                    else:
                        return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                gridMap = set()
                for col in range(3):
                    for row in range(3):
                        value = board[row+i][col+j]
                        if value != ".":
                            if value not in gridMap:
                                gridMap.add(value)
                            else:
                                return False
        return True
