class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []
        
        for j in range(n):
            # Check bounds (Your logic: only 1 index can violate at a time!)
            if q and q[0] <= j - k:
                q.popleft()
            
            # Evict smaller values from the back
            while q and nums[q[-1]] < nums[j]:
                q.pop()
                
            q.append(j)
            
            # Start tracking results once the first window is full
            if j >= k - 1:
                res.append(nums[q[0]])
                
        return res
