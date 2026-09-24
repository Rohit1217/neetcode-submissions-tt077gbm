from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            return 0

        n=len(nums)

        prefix_arr=[0]*n
        prefix_arr[0]=nums[0]

        for i in range(1,n):
            prefix_arr[i]=prefix_arr[i-1]+nums[i]
        

        target_hash=defaultdict(int)

        res=0

        for i in range(0,n):

            if prefix_arr[i]==k:
                res+=1

            res+=target_hash[prefix_arr[i]-k]

            target_hash[prefix_arr[i]]+=1
        
        return res