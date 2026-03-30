class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n=len(nums)        
        res_set=set()

        def twoSum(target,start):
            idx1=start-1
            end=n-1
            
            while start<end:
                val=nums[start]+nums[end]
                if val==target:
                    res_set.add((nums[idx],nums[start],nums[end]))
                    start+=1
                    end-=1
                
                elif val<target:
                    start+=1
                else:
                    end-=1
            return 

        res_list=[]
        for idx in range(n-1):
            target=-nums[idx]
            twoSum(target,idx+1)

        
        for res in res_set:
            res_list.append([res[0],res[1],res[2]])

        return res_list