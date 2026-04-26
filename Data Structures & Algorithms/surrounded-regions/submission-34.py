from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])

        if rows==0 or cols==0:
            return "EMPTY BOARD"

        res_board=[]
        queue=deque()
        visited=set()

        for row in range(rows):
            curr_row=[]
            for col in range(cols):
                curr_row.append("X")

                if (row==0 or col==0 or row==rows-1 or col==cols-1) and  board[row][col]=="O":
                    queue.append((row,col))
                    visited.add((row,col))
                    curr_row[-1]="O"

            res_board.append(curr_row)

        while len(queue)>0:
            curr_node=queue.popleft()
            row_idx,col_idx=curr_node

            neighbors=((row_idx-1,col_idx),(row_idx+1,col_idx),(row_idx,col_idx+1),(row_idx,col_idx-1))
            
            for neighbor in neighbors:
                n_row,n_col=neighbor[0],neighbor[1]
                if neighbor not in visited and n_row>-1 and n_row<rows and n_col<cols and n_col>-1 and board[n_row][n_col]=="O":
                    queue.append((n_row,n_col))
                    visited.add((n_row,n_col))
                    res_board[n_row][n_col]="O"
            

        for row in range(rows):
            for col in range(cols):
                board[row][col]=res_board[row][col]
                    

         
        