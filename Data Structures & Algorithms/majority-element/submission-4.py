from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_hash=defaultdict(int)
        for num in nums:
            count_hash[num]+=1
        for key in count_hash.keys():
            if count_hash[key]>=len(nums)//2:
                return key
            