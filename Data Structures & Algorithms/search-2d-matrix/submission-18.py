class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        left,right=0,rows*cols

        while left<right:
            mid=(left+right)//2
            r_idx,c_idx=mid//cols,mid%cols

            guess=matrix[r_idx][c_idx]
            if guess==target:
                return True
            elif guess<target:
                left=mid+1
            else:
                right=mid
        
        # print(left,right)
        # r_idx,c_idx=left//cols,left%cols
        # if matrix[r_idx][c_idx]==target:
        #     return True
        
        return False
