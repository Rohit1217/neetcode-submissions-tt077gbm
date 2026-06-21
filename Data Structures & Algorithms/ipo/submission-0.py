import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        cap_prof_arr=[]
        
        for p,c in zip(profits,capital):
            cap_prof_arr.append((-p,c))
        
        cap_prof_arr.sort(key=lambda k: k[1])
        curr_capital=w

        #BUILD HEAP 
        prof_heap=[]

        curr_idx=0
        
        while curr_idx<len(cap_prof_arr):
            p,c=cap_prof_arr[curr_idx]
            
            if c<=curr_capital:
                prof_heap.append((p,c))
                curr_idx+=1
            else:
                break
            # curr_idx+=1
        
        heapq.heapify(prof_heap)        
        count=0

        while count<k and prof_heap:
            p,c=heapq.heappop(prof_heap)
            curr_capital-=p

            while curr_idx<len(cap_prof_arr):
                p,c=cap_prof_arr[curr_idx]
                
                if c<=curr_capital:
                    heapq.heappush(prof_heap,(p,c))
                    curr_idx+=1
                else:
                    break
                
                # curr_idx+=1
            
            count+=1


        return curr_capital

            

