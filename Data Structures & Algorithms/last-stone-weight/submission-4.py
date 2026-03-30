import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones)==0:
            return 0


        stones=[-1*stone for stone in  stones]
        heapq.heapify(stones)  

        while len(stones)>1:
            maxm,second_maxm=heapq.heappop(stones),heapq.heappop(stones)
            if maxm==second_maxm:
                continue
            else:
                heapq.heappush(stones,-(second_maxm-maxm))
        
        if len(stones)==0:
            return 0
        else:
            return -stones[0]
        return 
        
        