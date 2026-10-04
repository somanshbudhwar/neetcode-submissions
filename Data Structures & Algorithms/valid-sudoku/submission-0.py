class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows():
            for row in range(0,9):
                nums=set()
                for i in board[row]:
                    if i==".":
                        continue
                    else:
                        if i in nums: return False
                        else: nums.add(i)
            return True

        def check_columns():
            for c in range(0,9):
                nums=set()
                col=[]
                for r in range(0,9):
                    col.append(board[r][c])
                for i in col:
                    if i==".":
                        continue
                    else:
                        if i in nums: return False
                        else: nums.add(i)
            return True

        def check_boxes():
            for c in range(0,9,3):
                for r in range(0,9,3):
                    nums=set()
                    x,y=(r,c)
                    for i in range(0,3):
                        for j in range(0,3):
                            if board[x+i][y+j]==".":
                                continue
                            else:
                                if board[x+i][y+j] in nums: return False
                                else: nums.add(board[x+i][y+j])
            return True

        if not check_rows():
            return False
        if not check_columns():
            return False
        if not check_boxes():
            return False
        return True


        