class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        combination=[]
        
        def combine_rec(i):
            if len(combination)==k:
                res.append(combination.copy())
                return

            elif i==n+1:
                return 
            
            combine_rec(i+1)

            combination.append(i)
            combine_rec(i+1)
            combination.pop()

            return
        
        combine_rec(1)
        return res