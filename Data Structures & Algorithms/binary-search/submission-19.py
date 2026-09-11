class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        #answer in arr[0,n]


        while left<right:
            mid=(left+right)//2

            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid
            else:
                return mid
        print(mid)
        return -1
        if nums[mid]!=target:
            return -1
        return mid