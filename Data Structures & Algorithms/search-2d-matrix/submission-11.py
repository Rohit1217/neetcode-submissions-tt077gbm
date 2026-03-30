class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows,cols=len(matrix),len(matrix[0])
        num_entries=rows*cols
        left=0
        right=num_entries-1
       
        while left<=right:
            mid=(right+left)//2
            mid_val=matrix[mid//cols][mid%cols]

            if mid_val==target:
                return True
            elif  mid_val<target:
                left=mid+1
            else:
                right=mid-1
        
        return False


        