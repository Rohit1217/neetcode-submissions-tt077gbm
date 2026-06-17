import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)

        if k>n//2:
            nums.sort(reverse=True)
            return nums[k-1]
        
        for i in range(n):
            nums[i]=-nums[i]

        heapq.heapify(nums)

        kth_max=None

        for i in range(k):
            curr_max=heapq.heappop(nums)
        
        kth_max=-curr_max
        return kth_max

        

