class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        guess_idx=len(nums)//3
        res_set=set()

        if len(nums)<3:
            return nums
        i=0    
        while guess_idx*i < len(nums):
            guess=nums[guess_idx*(i)]
            count=0
            
            for num in nums:
                if num==guess:
                    count+=1
            if count>len(nums)//3:
                res_set.add(guess)
            
            i+=1
        
        return list(res_set)
        