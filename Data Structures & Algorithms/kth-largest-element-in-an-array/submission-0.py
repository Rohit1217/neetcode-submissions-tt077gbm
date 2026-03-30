class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1

        if end < k-1:
            return -1
        k=len(nums)-k+1
        idx=nums[k - 1]
        
        def partition(start,end,k):
            idx = start + k - 1
            nums[idx], nums[end] = nums[end], nums[idx]
            val =  nums[end]
            store_idx = start
            
            for idx in range(start,end):
                if nums[idx]<val:
                    nums[idx],nums[store_idx]=nums[store_idx],nums[idx]
                    store_idx+=1
            
            nums[end],nums[store_idx]=nums[store_idx],nums[end]

            return store_idx

        start,end=0,len(nums)-1
        left,right=start,end
        curr_candidate=partition(start,end,k)
        
        while curr_candidate-start!=k-1:
            if curr_candidate-start<k-1:
                k=k-(curr_candidate-start+1)
                start=curr_candidate+1
            else:
                end=curr_candidate-1
            
            curr_candidate=partition(start,end,k)

        return nums[curr_candidate]



            
    
        