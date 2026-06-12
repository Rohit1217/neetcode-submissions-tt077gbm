class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        
        loc_hash={}
        loc=0
        for char in word:
            loc_hash[loc]=char
            loc+=1
        
        flag=False
        visited=set()

        def search_rec(r,c,idx):
            nonlocal flag

            if flag: return

            if idx==len(word):
                flag=True
                return

            if r<0 or r>rows-1 or c<0 or c>cols-1 or (r,c) in visited:
                return

            if board[r][c]!=word[idx]:
                return
            else:
                visited.add((r,c))
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    search_rec(r+dr, c+dc, idx+1)
                visited.remove((r,c))           
            return
        
        for row in range(rows):
            for col in range(cols):
                    search_rec(row,col,0)
                    if flag:
                        return True
        
        return False
                    

