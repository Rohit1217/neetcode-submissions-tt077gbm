from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count=defaultdict(int)
        
        for num in nums:
            num_count[num]+=1

        num_count_arr=[]
        
        for num in num_count:
            num_count_arr.append(((-1)*num_count[num],num))
         
        heapq.heapify(num_count_arr)
        count=0
        res_arr=[]

        while count<k:
            res_arr.append(heapq.heappop(num_count_arr)[1])
            count+=1

        return res_arr