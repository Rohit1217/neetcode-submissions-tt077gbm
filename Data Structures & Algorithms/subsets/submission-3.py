class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        global_res=[]

        def dfs(i,res):
            if i==len(nums):
                global_res.append(res.copy())
                return
            
            dfs(i+1,res)

            res.append(nums[i])
            dfs(i+1,res)
            res.pop()
            return
        
        dfs(0,[])
        return global_res
