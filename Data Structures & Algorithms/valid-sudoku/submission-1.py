class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def tile_check(tile_id)->bool:
            dim=3
            y=tile_id//dim*dim
            x=tile_id%dim*dim

            digits=set()

            for row in range(y,y+dim):
                for col in range(x,x+dim):
                    digit=board[row][col]
                    if digit==".":
                        continue
                    else:
                        if digit in digits:
                            print(row, col," Failed tile_check")
                            return False
                        else:
                            digits.add(digit)
            return True
        
        def row_check(row_id):
            digits=set()
            for col in range(9):
                digit=board[row_id][col]
                if digit==".":
                        continue
                if digit in digits:
                    # print(digits)
                    # print(digit)
                    # print(row_id, col," Failed row_check")
                    return False
                else:
                    digits.add(digit)
            return True
        
        def col_check(col_id):
            digits=set()
            for row in range(9):
                digit=board[row][col_id]
                if digit==".":
                        continue
                if digit in digits:
                    print(row, col_id," Failed col_check")
                    return False
                else:
                    digits.add(digit)
            return True


        for i in range(9):
            if row_check(i) and col_check(i) and tile_check(i):
                pass
            else:
                return False
        return True
        
