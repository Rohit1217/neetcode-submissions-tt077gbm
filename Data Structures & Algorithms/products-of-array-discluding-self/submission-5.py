class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr=[1 for _ in range(len(nums))]
        suffix_arr=[1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
                prefix_arr[i]=nums[i-1]*prefix_arr[i-1]
                suffix_arr[len(nums)-i-1]=nums[len(nums)-i]*suffix_arr[len(nums)-i]
        
        output_arr=[1 for _ in range(len(nums))]
        
        # print(prefix_arr,suffix_arr)
        for i,(pre,suf) in enumerate(zip(prefix_arr,suffix_arr)):
            output_arr[i]=pre*suf
            
        return output_arr