from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        rows,cols=len(board),len(board[0])
        visitable=set()
        
        for i in range(rows):
            for j in range(cols):
                if i==0 or j==0 or i==rows-1 or j==cols-1:
                    if board[i][j]=="O":
                        visitable.add((i,j))
                        q.append((i,j))
        print(q)
        while len(q)>0:
            i,j=q.popleft()
            neighbors=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for i_new,j_new in neighbors:
                if i_new<0 or j_new<0 or i_new>rows-1 or j_new>cols-1  or board[i_new][j_new]=="X":
                    continue
                elif (i_new,j_new) in visitable:
                    continue   
                else:
                    print(i_new,j_new,rows,cols)
                    q.append((i_new,j_new))
                    visitable.add((i_new,j_new))
        print(visitable)
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visitable:
                    board[i][j]="X"
    
        return
        

