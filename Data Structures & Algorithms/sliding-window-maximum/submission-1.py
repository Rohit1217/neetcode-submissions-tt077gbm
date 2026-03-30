import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n<k:
            return -1
        
        entry_finder=defaultdict(int)
        heap=[ -nums[idx] for idx in range(k)]
        heapq.heapify(heap)

        for val in heap:
            entry_finder[-val]+=1

        def add_val(idx : int):
            val=nums[idx]
            entry_finder[val]+=1
            heapq.heappush(heap,-val)
        
        def del_val(idx):
            val=nums[idx]
            entry_finder[val]-=1

        def extract_max():
            curr_val=heap[0]
            while entry_finder[-curr_val]<1:
                curr_val=heapq.heappop(heap)
                curr_val=heap[0]

            return -curr_val

        curr_max_list=[]
        for idx in range(k,n):
            val=extract_max()
            curr_max_list.append(val)
            del_val(idx-k)
            add_val(idx)
            
        
        curr_max_list.append(extract_max())
        
        return curr_max_list