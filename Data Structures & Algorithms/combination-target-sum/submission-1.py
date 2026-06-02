class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #OM NAMAH SHIVAY
        res=[]

        def backtrack(i,curr_target,curr_res):
            if curr_target==0:
                res.append(curr_res.copy())
                return
            elif i==len(nums) or curr_target<0:
                return

        
            backtrack(i+1,curr_target,curr_res)

            curr_res.append(nums[i])
            backtrack(i,curr_target-nums[i],curr_res)

            curr_res.pop()
            return

        backtrack(0,target,[])
        return res
            

