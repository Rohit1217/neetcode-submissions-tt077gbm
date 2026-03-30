class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n=len(nums)        
        res_set=set()
        res_list=[]
        
        def threeSum(target,idx1):
            def twoSum(target,idx1,idx2):
                start=idx2+1
                end=n-1
    
                while start<end:
                    val=nums[start]+nums[end]
                    if val==target:
                        # print(target,nums[idx1],nums[idx2])
                        res_set.add((nums[idx1],nums[idx2],nums[start],nums[end]))
                        start+=1
                        end-=1
                                    
                    elif val<target:
                        start+=1
                    else:
                        end-=1
                return 

            for idx2 in range(idx1+1,n-1):
                curr_target=target-nums[idx2]
                # print(curr_target)
                twoSum(curr_target,idx1,idx2)

        
        for idx1 in range(n-2):
            curr_target=target-nums[idx1]
            # print(curr_target,target)
            threeSum(curr_target,idx1)

        for res in res_set:
            res_list.append([res[0],res[1],res[2],res[3]])

        return res_list


        