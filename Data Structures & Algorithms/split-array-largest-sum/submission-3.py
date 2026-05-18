class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        right=sum(nums)
        left=max(nums)

        if k>len(nums):
            return False

        def is_split(target):
            i=0
            l=[]
            count=0
            curr_sum=0
            for j in range(len(nums)):
                
                if nums[j]>target:
                    return False
                
                curr_sum+=nums[j]
                if curr_sum>target:
                    l.append((i,j))
                    i=j
                    curr_sum=nums[j]
                    count+=1
                    
            count+=1           
            if count<=k:
                return True

            return False

        ans=right

        while left<=right:
            mid=(left+right)//2

            if is_split(mid):
                right=mid-1
                ans=mid
            else:
                left=mid+1
        
        return ans
