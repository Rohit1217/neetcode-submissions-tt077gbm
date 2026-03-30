class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_mult=1
        zero_count=0
        for num in nums:
            if num!=0:
                non_zero_mult*=num
            else:
                zero_count+=1
        if zero_count>1:
            return [0 for num in nums]        
        arr=[]

        for num in nums :
            if num!=0 and zero_count==1:
                arr.append(0)
            elif num==0:
                arr.append(non_zero_mult) 
            else:
                arr.append(non_zero_mult//num)
        return arr       