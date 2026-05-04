class Solution:
    def findMin(self, nums: List[int]) -> int:

        # 1 2 3 4 5 6 7
        # 6 7 1 2 3 4 5

        n=len(nums)
        if n==0:
            return False
        elif n==1 or n==2:
            return min(nums)
            
        def get_neighbor(idx):
            succ=(idx+1)%n
            prev=(idx-1)%n
            return prev,succ

        left,right=0,n-1

        if nums[0]<nums[-1]:
            return nums[0]
        elif nums[-1]<nums[-2]:
            return nums[-1]

        
        while left<right:
            mid=(left+right)//2
            print(left,right,mid)
            if nums[mid]>nums[(mid+1)%n] and nums[mid]>nums[(mid-1)%n]:
                return nums[(mid+1)%n]
            elif nums[(mid-1)%n]>nums[mid] and nums[mid]<nums[(mid+1)%n]:
                return nums[mid]

            elif nums[mid]>nums[left]:
                left=mid+1
            else:
                right=mid

        return nums[right]

 
            


