class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        prefix_sum_arr=[]
        target_prefix_sum_hash={}
        count=0

        for idx in range(len(nums)):
            prefix_sum=nums[idx]+prefix_sum
            curr_val=prefix_sum
            curr_target=curr_val-k

            if curr_target in target_prefix_sum_hash:
                count+=len(target_prefix_sum_hash[curr_target])
            if curr_target==0:
                count+=1

            prefix_sum_arr.append(nums[idx]+prefix_sum)
            
            if curr_val in target_prefix_sum_hash:
                target_prefix_sum_hash[curr_val].append(idx)
            else:
                target_prefix_sum_hash[curr_val]=[idx]
        return count