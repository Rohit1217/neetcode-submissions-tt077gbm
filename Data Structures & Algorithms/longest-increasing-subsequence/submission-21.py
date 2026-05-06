class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n=len(nums)
        lis=[1]*n
        prev=list(range(n))
        
        for i in range(1,n):            
            for j in range(i):
                
                if nums[i]>nums[j]:
                    val=max(lis[i],1+lis[j])
                    
                    if val>lis[i]:
                        lis[i]=val
                        prev[i]=j
        

        max_idx=0
        max_val=1

        for idx in range(n):
            if lis[idx]>max_val:
                max_idx=idx
                max_val=lis[idx]
        
        seq=[]
        print(prev)
        while prev[idx]!=idx:
            seq.append(nums[idx])
            idx=prev[idx]
        seq.append(nums[idx])
        

        return max_val
                