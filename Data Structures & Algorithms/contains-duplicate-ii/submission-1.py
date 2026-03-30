class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window=set()
        idx=0
        
        for num in nums:
            if num in window:
                return True
            else:
                window.add(num)

            if len(window)>k:
                window.remove(nums[idx-k])
            idx+=1
        
        return False