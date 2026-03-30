class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        if candidates==[]:
            return res
        
        candidates.sort()
        
        def combinationSum2_rec(target,start_idx,curr_sol):
            print(start_idx,target,curr_sol)
            if target==0:
                res.append(list(curr_sol))
            elif start_idx==len(candidates):
                return
            elif target-candidates[start_idx]<0:
                return
            else:
                for idx in range(start_idx,len(candidates)):
                    if idx>start_idx and candidates[idx]==candidates[idx-1]:
                        continue
                        
                    candidate=candidates[idx]
                    curr_sol.append(candidate)
                    combinationSum2_rec(target-candidate,idx+1,curr_sol)
                    curr_sol.pop()
                return
        
        combinationSum2_rec(target,0,[])
        # res=list(res)
        # res=[list(sub_res) for sub_res in res]
        return res
