class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]

        if nums==[]:
            return res
        
        minm=min(nums)

        def combinationSum_rec(nums,target,start_idx,minm,curr_sol):
            if target==0:
                res.append(curr_sol)
                return            
            if target-minm<0:
                return 
            else:
                for idx in range(start_idx,len(nums)):
                    num=nums[idx]
                    combinationSum_rec(nums,target-num,idx,minm,curr_sol+[num])                    
                return


        combinationSum_rec(nums,target,0,minm,[])
        return res
