class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        #OM NAMAH SHIVAY
        res=[]
        nums.sort()
        path=[]

        def backtrack(i,curr_target):
            if curr_target==0:
                res.append(path.copy())
                return
            elif i==len(nums) or curr_target<0:
                return

            j=i
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            
            if j<len(nums):
                backtrack(j,curr_target)

            path.append(nums[i])
            backtrack(i+1,curr_target-nums[i])

            path.pop()
            return

        backtrack(0,target)
        return res
            

