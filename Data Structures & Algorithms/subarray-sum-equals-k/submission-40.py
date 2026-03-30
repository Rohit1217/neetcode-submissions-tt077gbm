from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        target_prefix_sum_hash = defaultdict(int)
        target_prefix_sum_hash[0] = 1
        count = prefix_sum = 0
        
        get = target_prefix_sum_hash.get
        inc = target_prefix_sum_hash.__setitem__

        for num in nums:
            prefix_sum += num
            count += get(prefix_sum - k, 0)
            inc(prefix_sum, target_prefix_sum_hash[prefix_sum] + 1)

        return count