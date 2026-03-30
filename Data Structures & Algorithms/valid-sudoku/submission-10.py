class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash={}
        col_hash={}
        sub_matrix_hash={}
        #Initalization
        for i in range(9):
            row_hash[i]={}
            col_hash[i]={}
            sub_matrix_hash[i]={}
        
        for i in range(9):
            for j in range(9):
                #Row check
                if board[i][j]==".":
                    continue
                try: 
                  row_hash[i][board[i][j]]+=1
                  return False
                except Exception as e:
                  row_hash[i][board[i][j]]=1 
                #Column check
                try:
                   col_hash[j][board[i][j]]+=1
                   return False
                except Exception as e:
                   col_hash[j][board[i][j]]=1 
                #SubMatrix check
                index=(i//3)*3+(j//3)
                try:
                   sub_matrix_hash[index][board[i][j]]+=1
                   return False
                except Exception as e:
                   sub_matrix_hash[index][board[i][j]]=1 

        return True