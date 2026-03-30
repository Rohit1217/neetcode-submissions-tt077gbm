class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        num_matrix=matrix
        num_rows=len(matrix)
        num_cols=len(matrix[0])
        self.presum_matrix = [[0]*num_cols for _ in range(num_rows)]

        sums=0
        for row in range(num_rows):
            self.presum_matrix[row][0]=sums + num_matrix[row][0]
            sums=sums + num_matrix[row][0]

        sums=0
        for col in range(num_cols):
            self.presum_matrix[0][col]=sums +num_matrix[0][col]
            sums=self.presum_matrix[0][col]

        col_idx=1
        while col_idx<num_cols:
            for row_idx in range(1,num_rows):
                self.presum_matrix[row_idx][col_idx]=self.presum_matrix[row_idx][col_idx-1]+self.presum_matrix[row_idx-1][col_idx]-self.presum_matrix[row_idx-1][col_idx-1] + num_matrix[row_idx][col_idx]
            col_idx+=1

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1==0 and row1==0:
            return self.presum_matrix[row2][col2]
        elif col1==0:
            return self.presum_matrix[row2][col2]-self.presum_matrix[row1-1][col2]
        elif row1==0:
            return self.presum_matrix[row2][col2]-self.presum_matrix[row2][col1-1]
        else:
            return self.presum_matrix[row2][col2]-self.presum_matrix[row1-1][col2]-self.presum_matrix[row2][col1-1]+self.presum_matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)