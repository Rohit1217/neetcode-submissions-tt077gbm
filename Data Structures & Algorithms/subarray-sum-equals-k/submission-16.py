class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        target_prefix_sum_hash={}
        count=0

        for idx in range(len(nums)):
            prefix_sum=nums[idx]+prefix_sum
            curr_target=prefix_sum-k

            if curr_target in target_prefix_sum_hash:
                count+=len(target_prefix_sum_hash[curr_target])
            if curr_target==0:
                count+=1

            if prefix_sum in target_prefix_sum_hash:
                target_prefix_sum_hash[prefix_sum].append(idx)
            else:
                target_prefix_sum_hash[prefix_sum]=[idx]
        return count