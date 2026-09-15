class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        curr_res=[]

        def comb_rec(i):
            if len(curr_res)==k:
                res.append(curr_res.copy())
            elif i>=n:
                return
            else:
                for j in range(i+1,n+1):
                    curr_res.append(j)
                    comb_rec(j)      
                    curr_res.pop()
                return                  

        comb_rec(0)
        return res