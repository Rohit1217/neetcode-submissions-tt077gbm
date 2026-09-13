
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])

        visited=set()
        queue=deque()

        for r in range(rows):
            if board[r][cols-1]=="O":
                queue.append((r,cols-1))
                visited.add((r,cols-1))
            if board[r][0]=="O":
                queue.append((r,0))        
                visited.add((r,0))
        
        for c in range(cols):
            if board[rows-1][c]=="O":
                queue.append((rows-1,c))
                visited.add((rows-1,c))
            if board[0][c]=="O":
                queue.append((0,c)) 
                visited.add((0,c))

        while queue:
            r,c=queue.popleft()

            neighbors=[(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

            for nr,nc in neighbors:
                if nr<0 or nc<0 or nr>rows-1 or nc>cols-1 or (nr,nc) in visited or board[nr][nc]=="X":
                    continue
                
                queue.append((nr,nc))
                visited.add((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in visited:
                    board[r][c]="X"
        
        return

