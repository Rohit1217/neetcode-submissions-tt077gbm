class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left=0
        right=len(nums)-1
        guess=(left+right)//2

        # if  nums[0]>target:
        #     return 0
        # elif nums[len(nums)-1]<target:
        #     return len(nums)

        while left<=right:
            if nums[guess]==target:
                print(guess,True)
                return guess
            elif nums[guess]>target:
                right=guess-1
            else:
                left=guess+1

            guess=(left+right)//2



        return left