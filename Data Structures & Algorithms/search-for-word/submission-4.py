class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        if len(board)==0:
            return False
        
        visited=set()
        self.flag=False
        rows,cols=len(board),len(board[0])
        
        def exist_back(row,col,search_idx): 
            if search_idx==len(word):
                self.flag=True
                return 
            elif self.flag==True:
                return
            
            elif row<0 or col<0 or row>rows-1 or col>cols-1 or (row,col) in visited or board[row][col]!=word[search_idx]:
                return
            else:
                
                visited.add((row,col))
                exist_back(row-1,col,search_idx+1)
                exist_back(row+1,col,search_idx+1)
                exist_back(row,col+1,search_idx+1)
                exist_back(row,col-1,search_idx+1)
                visited.remove((row,col))
        
            return
        
        for row in range(rows):
            for col in range(cols):
                exist_back(row,col,0)
                visited.clear()
                if self.flag==True:
                    return self.flag
        
        return self.flag

                
        