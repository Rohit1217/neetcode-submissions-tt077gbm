class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])

        rows_kill=set()
        cols_kill=set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    rows_kill.add(row)
                    cols_kill.add(col)

        for row in rows_kill:
            for col in range(cols):
                matrix[row][col]=0
        

        for col in cols_kill:
            for row in range(rows):
                matrix[row][col]=0
        





        
        