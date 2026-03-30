class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows,cols=len(matrix),len(matrix[0])
        num_entries=rows*cols
        left=0
        right=num_entries-1
       
        while (right-left)>1:
            mid=(right+left)//2
            mid_val=matrix[mid//cols][mid%cols]

            if mid_val==target:
                return True
            elif  mid_val<target:
                left=mid
            else:
                right=mid
        
        if matrix[left//cols][left%cols]==target or matrix[right//cols][right%cols]==target:
            return True
        
        return False


        