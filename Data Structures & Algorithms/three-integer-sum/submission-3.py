class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]
        last_i=0
        for i in range(len(nums)):
            if last_i!=i and nums[last_i]==nums[i]:
                continue
            j=i+1
            k=len(nums)-1
            target=-nums[i]
            last_num1=-1e-8
            while j<k:
                # print(j,k)
                num1,num2=nums[j],nums[k]
                sums=num1+num2
                if sums==target and last_num1!=num1:
                    results.append([-target,num1,num2])
                    j=j+1
                    k=k-1
                    last_num1=num1
                elif sums>target:
                    k=k-1
                else:
                    j=j+1     
            last_i=i
        return results
        