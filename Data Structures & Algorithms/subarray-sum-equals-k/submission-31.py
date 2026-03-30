from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        target_prefix_sum_hash=defaultdict(int)
        target_prefix_sum_hash[0]=1
        count=0

        for idx in range(len(nums)):
            prefix_sum=nums[idx]+prefix_sum
            count+=target_prefix_sum_hash[prefix_sum-k]
            target_prefix_sum_hash[prefix_sum]+=1

        return count