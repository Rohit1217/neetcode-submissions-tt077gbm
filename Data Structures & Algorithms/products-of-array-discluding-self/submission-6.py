class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr=[1 for idx in range(len(nums))]
        suffix_arr=[1 for idx in range(len(nums))]

        # nums=[1]+nums+[1]
        prefix=1
        suffix=1

        for idx in range(0,len(nums)):
            prefix_arr[idx]=prefix*nums[idx]
            prefix=prefix*nums[idx]
        
        for idx in range(len(nums)-1,-1,-1):
            suffix=suffix*nums[idx]
            suffix_arr[idx]=suffix
        
        print(prefix_arr,suffix_arr)

        prefix_arr=[1]+prefix_arr+[1]
        suffix_arr=[1]+suffix_arr+[1]

        res=[]
        for idx in range(1,len(nums)+1):
            res.append(prefix_arr[idx-1]*suffix_arr[idx+1])
        
        return res