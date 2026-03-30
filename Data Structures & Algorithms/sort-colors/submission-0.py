class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_list=[0]*3

        for num in nums:
            count_list[num]+=1
        
        for idx in range(count_list[0]):
            nums[idx]=0
        
        for idx in range(count_list[0],count_list[0]+count_list[1]):
            nums[idx]=1        

        for idx in range(count_list[1]+count_list[0],count_list[1]+count_list[0]+count_list[2]):
            nums[idx]=2
        
        return 



