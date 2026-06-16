class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        free_positions=set((i,j) for i in range(n) for j in range(n))
        
        res_count=0
        curr_state=[]


        def totalNQueens_rec(c):
            nonlocal res_count
            
            if c==n:
                res_count+=1
                return
            elif len(free_positions)==0:
                return
            else:
                for r in range(n):
                    pos=(r,c)
                    flag=True

                    for used_pos in curr_state:
                        used_r,used_c=used_pos
                        
                        if used_r==r or used_c==c:
                            flag=False
                            break
                        elif abs(used_r-r)==abs(used_c-c):
                            flag=False
                            break
                    
                    if flag:     
                        curr_state.append(pos)
                        totalNQueens_rec(c+1)
                        curr_state.pop()

        totalNQueens_rec(0)
        
        return res_count

                        
