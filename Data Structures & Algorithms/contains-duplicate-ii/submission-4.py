from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos_hash={}

        for idx in range(len(nums)):
            val=nums[idx]
            
            if val in pos_hash:                
                prev_idx=pos_hash[val]
                if idx-prev_idx<=k:
                    return True
            
            pos_hash[val]=idx
        
        return False
        