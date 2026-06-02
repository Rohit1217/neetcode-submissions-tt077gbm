from collections import Counter,defaultdict

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        #OM NAMAH SHIVAY
        res=[]
        nums.sort()

        pos=defaultdict(lambda: len(nums))
        
        for i in range(len(nums)):
            pos[nums[i]]=min(pos[nums[i]],i)

        def backtrack(i,curr_target,curr_res):
            if curr_target==0:
                res.append(curr_res.copy())
                return
            elif i==len(nums) or curr_target<0:
                return

            j=i
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            
            if j<len(nums):
                backtrack(j,curr_target,curr_res)

            curr_res.append(nums[i])
            backtrack(i+1,curr_target-nums[i],curr_res)

            curr_res.pop()
            return

        backtrack(0,target,[])
        return res
            

