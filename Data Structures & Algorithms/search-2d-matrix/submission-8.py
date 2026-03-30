class Solution:

    def searchList(self,row:List[int],target:int) -> bool:
        left,right=0,len(row)
        while right-left>1:
            search_idx=(left+right)//2
            if row[search_idx]==target:
                return True
            elif row[search_idx]<target:
                left=search_idx
            else:
                right=search_idx

        search_idx=(left+right)//2
        if row[search_idx]==target:
            return True

        return False    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_strt,row_end,col_strt,col_end=0,len(matrix),0,len(matrix[0])
        row_idx,col_idx=(row_end-row_strt)//2,(col_end-col_strt)//2

        while row_end-row_strt>1:
            val=matrix[row_idx][col_idx]
            if val==target:
                return True
            elif val>target:
                if matrix[row_idx][0]>target:
                    row_end=row_idx
                else:
                    return self.searchList(matrix[row_idx],target)
            else:
                if matrix[row_idx][col_end-1]<target:
                    row_strt=row_idx+1
                else:
                    return self.searchList(matrix[row_idx],target)
            row_idx=(row_end+row_strt)//2

        if row_idx>=len(matrix):
            return False
        return  self.searchList(matrix[row_idx],target)




        