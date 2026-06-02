from collections import Counter

class Solution:
    def __init__(self):
        self.res_sum=0

    def subsetXORSum(self, nums: List[int]) -> int:

        def xor():
            res=0
            for j in range(0,len(nums)):
                res=res^nums[j]
            return res

        def xor_rec(i):
            
            for k in range(2):
                val_i=nums[i]
            
                if k==0:
                    nums[i]=0

                if i==len(nums)-1:
                    self.res_sum+=xor()
                else:
                    xor_rec(i+1)
                
                nums[i]=val_i
            
            return 
        
        xor_rec(0)
        return self.res_sum