class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pat=[nums[0]]


        def bin_search(n,t):
            left=0
            right=n

            while left<right:
                mid=(left+right)//2

                if pat[mid]>t:
                    right=mid
                elif pat[mid]<t:
                    left=mid+1
                else:
                    return mid
            return left
        

        for i in range(1,len(nums)):
            target=nums[i]
            k=bin_search(len(pat),target)

            if k==len(pat):
                pat=pat+[nums[i]]
            else:
                pat[k]=nums[i]
        
        return len(pat)