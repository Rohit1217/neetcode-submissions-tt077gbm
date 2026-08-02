class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp={}
        n=len(nums)

        def findTarget(i,t):
            if t==0 and i==n:
                return 1
            elif i==n:
                return 0
            elif (i,t) in dp:
                return dp[(i,t)]
            else:
                count=findTarget(i+1,t-nums[i])
                count+=findTarget(i+1,t+nums[i])

            dp[(i,t)]=count
            return count

        return findTarget(0,target)    
            


