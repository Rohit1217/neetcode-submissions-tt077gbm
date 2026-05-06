class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0:
            return 
    
        target_twice=sum(nums)
        
        if target_twice%2!=0:
            return False
        else:
            target=target_twice//2
        

        val=[0]*(target+1)
        val[0]=1

        for i in range(n):
            for j in range(target,0,-1):
                if j-nums[i]>-1:
                    # print(val,i,j)
                    val[j]=val[j] or val[j-nums[i]]


        if val[target]==1:
            return True
        
        return False