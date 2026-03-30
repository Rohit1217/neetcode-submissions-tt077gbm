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
                  print(row_hash[i])
                  return False
                except Exception as e:
                  row_hash[i][board[i][j]]=1 
                #Column check
                try:
                   if j==3:
                    print(board[i][j],i,j)
                   col_hash[j][board[i][j]]+=1
                   print(col_hash[j],j)
                   return False
                except Exception as e:
                   col_hash[j][board[i][j]]=1 
                #SubMatrix check
                index=(i//3)*3+(j//3)
                try:
                   sub_matrix_hash[index][board[i][j]]+=1
                   print(sub_matrix_hash[index])
                   return False
                except Exception as e:
                   sub_matrix_hash[index][board[i][j]]=1 
        # for i in range(8):
        #     print(list(row_hash[i].keys()))
        #     print(list(col_hash[i].keys()))
        #     print(list(sub_matrix_hash[i].keys()))

        #     if list(row_hash[i].keys())==[]:
        #         return False
        #     if list(col_hash[i].keys())==[]:
        #         return False
        #     if list(sub_matrix_hash[i].keys())==[]:
        #         return False
        return True