from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        target_prefix_sum_hash=defaultdict(int)
        target_prefix_sum_hash[0]=1
        count=0

        for idx in range(len(nums)):
            prefix_sum=nums[idx]+prefix_sum
            curr_target=prefix_sum-k

            if curr_target in target_prefix_sum_hash:
                count+=target_prefix_sum_hash[curr_target]
                
            target_prefix_sum_hash[prefix_sum]+=1

        return count