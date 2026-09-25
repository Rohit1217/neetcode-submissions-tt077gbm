class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)

        res=[]
        curr_res=[]

        def combsum_rec(i,t):
            if t==0:
                res.append(curr_res.copy())
                return
            elif i==n or t<0:
                return
            
            curr_res.append(nums[i])
            combsum_rec(i,t-nums[i])
            curr_res.pop()
            combsum_rec(i+1,t)
        
        combsum_rec(0,target)
        return res

