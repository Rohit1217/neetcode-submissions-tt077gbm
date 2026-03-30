class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows,cols=len(matrix),len(matrix[0])
        if rows==0 or cols==0:
            return 0
        
        for row in range(rows):
            for col in range(row,cols):
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
        print(matrix)
        for col in range(cols//2):
            for row in range(rows):
                matrix[row][col],matrix[row][cols-col-1]=matrix[row][cols-col-1],matrix[row][col]

        return
        