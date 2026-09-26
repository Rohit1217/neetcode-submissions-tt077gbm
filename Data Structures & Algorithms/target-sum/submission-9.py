class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=[{} for i in range(len(nums))]

        n=len(nums)

        def find_target_rec(i,t):
            if t==0 and i==n:
                return 1
            elif  i==n:
                return 0
            elif t in memo[i]:
                return memo[i][t]
            else:
                count=0
                
                count+=find_target_rec(i+1,t-nums[i])
                count+=find_target_rec(i+1,t+nums[i])

                memo[i][t]=count
                return count
        
        res=find_target_rec(0,target)
        # print(memo)
        return res