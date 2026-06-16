class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        free_positions=set((i,j) for i in range(n) for j in range(n))
        
        res_positions=[]
        curr_state=[]

        def create_board_positons(stack):
            board=[]
            for i in range(n):
                pos_str=""
                for j in range(n):
                    if (i,j) in stack:
                        pos_str+="Q"
                    else:
                        pos_str+="."
                board.append(pos_str)
            return board

        def solveNQueens_rec(c):
            if c==n:
                res_positions.append(create_board_positons(curr_state))
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
                        solveNQueens_rec(c+1)
                        curr_state.pop()

        solveNQueens_rec(0)
        
        return res_positions

                        
