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

        def search_neighbor(pos,direc,num_matches):
            r_idx,c_idx=pos

            if direc=="left":
                c_idx-=1
            elif direc=="right":
                c_idx+=1
            elif direc=="top":
                r_idx+=1
            elif direc=="down":
                r_idx-=1
            
            if (r_idx,c_idx) in visited:
                return
            
            search_rec((r_idx,c_idx),num_matches)
            return


        def search_rec(pos,num_matches):
            nonlocal flag

            if num_matches==len(word):
                flag=True
                return

            r_idx,c_idx=pos
            if r_idx<0 or r_idx>rows-1 or c_idx<0 or c_idx>cols-1 or (r_idx,c_idx) in visited:
                return


            if board[r_idx][c_idx]!=loc_hash[num_matches]:
                return
            else:
                num_matches+=1
                visited.add((r_idx,c_idx))

                for direc in ["left","right","top","down"]:
                    search_neighbor(pos,direc,num_matches)
                
                num_matches-=1
                visited.remove((r_idx,c_idx))            
            return
        
        for row in range(rows):
            for col in range(cols):
                    search_rec((row,col),0)
                    if flag==True:
                        return True
        
        return False
                    

