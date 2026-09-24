class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #binary k
        n=len(nums)

        if k>n:
            return -1

        def is_splittable(s):
            if s<max(nums):
                return 0

            j=0
            prefix=0
            count=0

            while j<n:
                prefix+=nums[j]

                if prefix>s:
                    prefix=0
                    j=j-1
                    count+=1
                
                j+=1

            if prefix!=0:
                count+=1
            
            if count>k:
                return 0
            return 1
        
        l=0
        r=sum(nums)
        print(is_splittable(16))

        while l<r:
            mid=(l+r)//2

            if is_splittable(mid):
                r=mid
            else:
                l=mid+1
        
        return l

